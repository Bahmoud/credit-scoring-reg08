import streamlit as st
import requests

# ======================
# CONFIGURATION PAGE
# ======================
st.set_page_config(page_title="Credit Scoring", layout="centered")

# ======================
# STYLE VISUEL GLOBAL
# ======================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}
.main {
    background: rgba(255,255,255,0.04);
    padding: 30px;
    border-radius: 15px;
}
h1, h2, h3 {
    color: white;
}
.stNumberInput input, .stSelectbox div {
    background-color: rgba(255,255,255,0.08);
    color: white;
    border-radius: 10px;
}
.stButton button {
    background: linear-gradient(90deg, #00ff87, #60efff);
    border-radius: 12px;
    height: 60px;
    font-size: 18px;
    font-weight: bold;
    color: black;
    border: none;
    width: 100%;
    transition: 0.3s;
}
.stButton button:hover {
    transform: scale(1.03);
    box-shadow: 0px 0px 20px #00ff87;
}
</style>
""", unsafe_allow_html=True)

# ======================
# TITRE
# ======================
st.title("💳 Credit Scoring - REG08")
st.write("Simulation du risque de défaut d’un client")
st.header("Informations client")

# ======================
# SCORES EXTERNES
# ======================
EXT_SOURCE_1 = st.slider("Score de solvabilité externe 1", 0.0, 1.0, 0.5)
EXT_SOURCE_2 = st.slider("Score de solvabilité externe 2", 0.0, 1.0, 0.5)
EXT_SOURCE_3 = st.slider("Score de solvabilité externe 3", 0.0, 1.0, 0.5)

# ======================
# CREDIT
# ======================
col1, col2 = st.columns(2)
with col1:
    AMT_CREDIT = st.number_input("Montant du crédit", 10000, 2000000, 500000)
with col2:
    AMT_ANNUITY = st.number_input("Mensualité", 1000, 100000, 25000)
AMT_GOODS_PRICE = st.number_input("Valeur du bien financé", 10000, 2000000, 450000)

# ======================
# PROFIL CLIENT
# ======================
age = st.slider("Âge du client", 18, 70, 35)
anciennete = st.slider("Ancienneté professionnelle (années)", 0, 40, 5)
col3, col4 = st.columns(2)
with col3:
    statut_familial = st.selectbox("Situation familiale", ["Célibataire", "Marié"])
with col4:
    profession = st.selectbox(
        "Profession du client",
        ["Cadre / Employé", "Indépendant", "Salarié manuel (ouvrier)", "Autre"]
    )
married_value = 1 if statut_familial == "Marié" else 0
laborer_value = 1 if profession == "Salarié manuel (ouvrier)" else 0

# ======================
# TRADUCTION FEATURES
# ======================
TRADUCTION_FEATURES = {
    "EXT_SOURCE_1": "Score de solvabilité externe",
    "EXT_SOURCE_2": "Historique financier externe",
    "EXT_SOURCE_3": "Fiabilité de paiement externe",
    "AMT_GOODS_PRICE": "Valeur du bien financé",
    "AMT_CREDIT": "Montant du crédit demandé",
    "AMT_ANNUITY": "Charge mensuelle du crédit",
    "DAYS_BIRTH": "Âge du client",
    "DAYS_EMPLOYED": "Stabilité professionnelle",
    "NAME_FAMILY_STATUS_Married": "Situation familiale",
    "OCCUPATION_TYPE_Laborers": "Type d’emploi"
}

# ======================
# NIVEAU DE RISQUE
# ======================
def niveau_risque(proba: float) -> str:
    if proba < 0.2:
        return "Faible"
    elif proba < 0.5:
        return "Moyen"
    else:
        return "Élevé"

# ======================
# URL DE L’API (à remplacer par celle de Render ou autre)
# ======================
API_URL = "https://credit-scoring-reg08-1.onrender.com/"

# ======================
# PREDICTION VIA API
# ======================
if st.button("Analyser le risque"):

    data = {
        "EXT_SOURCE_1": EXT_SOURCE_1,
        "EXT_SOURCE_2": EXT_SOURCE_2,
        "EXT_SOURCE_3": EXT_SOURCE_3,
        "AMT_GOODS_PRICE": AMT_GOODS_PRICE,
        "AMT_ANNUITY": AMT_ANNUITY,
        "AMT_CREDIT": AMT_CREDIT,
        "DAYS_BIRTH": -age*365,
        "DAYS_EMPLOYED": -anciennete*365,
        "DAYS_LAST_PHONE_CHANGE": -1000,
        "NAME_FAMILY_STATUS_Married": married_value,
        "REGION_RATING_CLIENT": 2,
        "REGION_RATING_CLIENT_W_CITY": 2,
        "FLAG_DOCUMENT_3": 1,
        "DAYS_ID_PUBLISH": -3000,
        "OCCUPATION_TYPE_Laborers": laborer_value
    }

    try:
        response = requests.post(API_URL, json=data, timeout=10)

        if response.status_code != 200:
            st.error("Erreur côté API")
            st.write(response.text)
        else:
            result = response.json()
            proba = result["probabilite_defaut"]
            decision = result["decision"]
            facteurs = result.get("facteurs_principaux", [])

            st.divider()
            st.subheader("Décision de crédit")
            st.progress(min(max(proba, 0.0), 1.0))
            st.write(f"Risque estimé : **{proba:.1%}**")
            st.write(f"Niveau de risque : **{niveau_risque(proba)}**")
            st.write("✅ Crédit accordé" if decision=="ACCORDÉ" else "❌ Crédit refusé")

            st.subheader("Pourquoi cette décision ?")
            if facteurs:
                for f in facteurs:
                    nom_tech = f["feature"]
                    nom_client = TRADUCTION_FEATURES.get(nom_tech, "Facteur du dossier")
                    impact = f["impact"]
                    if impact < 0:
                        st.success(f"✔ {nom_client} améliore la fiabilité")
                    else:
                        st.warning(f"⚠ {nom_client} augmente le niveau de risque")
            else:
                st.info("Aucune explication disponible.")

    except requests.exceptions.RequestException as e:
        st.error("Impossible de contacter l’API")
        st.write(str(e))
