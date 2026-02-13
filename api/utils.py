import joblib
import pandas as pd
import shap

pipeline = joblib.load("models/credit_scoring_model.pkl")

# 🔹 Récupérer le dernier élément du pipeline (le modèle ML)
model = list(pipeline.named_steps.values())[-1]

feature_names = pipeline.feature_names_in_

explainer = shap.TreeExplainer(model)

def predict_client(data_dict):

    df = pd.DataFrame([data_dict])
    df = df.reindex(columns=feature_names, fill_value=0)

    proba = pipeline.predict_proba(df)[0, 1]
    decision = "REFUSÉ" if proba > 0.5 else "ACCORDÉ"

    top_factors = []

    try:
        shap_values = explainer.shap_values(df)

        contributions = pd.DataFrame({
            "feature": df.columns,
            "impact": shap_values[0]
        }).sort_values(by="impact", key=abs, ascending=False)

        top_factors = contributions.head(5).to_dict(orient="records")

    except Exception as e:
        print("SHAP non disponible:", e)

    return {
        "probabilite_defaut": float(proba),
        "decision": decision,
        "facteurs_principaux": top_factors
    }
