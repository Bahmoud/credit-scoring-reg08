# Credit Scoring Machine Learning — Projet REG08

## Objectif du projet
Ce projet vise à construire un système de **scoring de crédit automatisé** capable de :

- estimer la probabilité de défaut d’un client  
- aider à la décision d’octroi de crédit  
- expliquer la décision du modèle (interprétabilité)  
- proposer une interface utilisateur simple (dashboard Streamlit)  
- exposer le modèle via une API FastAPI  
- suivre et versionner les expérimentations ML avec **MLflow**

Le projet suit une démarche complète de **Data Science** et **MLOps**.

---

## Problème métier

Une institution financière souhaite :

✔ évaluer le risque de défaut d’un client  
✔ automatiser la décision d’octroi de crédit  
✔ comprendre pourquoi une décision est prise  
✔ disposer d’un outil utilisable par un conseiller  

Le modèle prédit donc :

- Probabilité de défaut  
- Décision crédit (accordé ou refusé)  
- Facteurs explicatifs de la décision  

---

## Jeux de données utilisés

Les données proviennent du projet **Home Credit Default Risk**.  
Lien : [Google Drive](https://drive.google.com/drive/folders/1C_ic7Qp8Vti6A2I3IxGifAXiWKHQJMbt?usp=sharing)

- **application_train** : caractéristiques personnelles, financières et de crédit  
- **bureau** : historique des crédits passés  
- **bureau_balance** : évolution mensuelle des crédits  
- **previous_application** : demandes de crédit antérieures  

---

## Feature Engineering

Les étapes réalisées :

✔ fusion des datasets  
✔ création de variables agrégées  
✔ gestion des valeurs manquantes  
✔ encodage des variables catégorielles  
✔ normalisation si nécessaire  

Exemples : agrégation historique, indicateurs de stabilité financière, variables de comportement client.

---

## Modélisation

### Modèles testés
- Régression logistique  
- Random Forest  
- Gradient Boosting (**modèle retenu**)  

**Gradient Boosting** choisi pour :  
- bonnes performances sur données tabulaires  
- gestion des relations non linéaires  
- robustesse aux variables nombreuses  
- bon compromis biais / variance

---

## Pipeline Machine Learning

**Prétraitement → Transformation → Modèle → Prédiction**

Avantages :  
✔ reproductibilité  
✔ cohérence entre entraînement et prédiction  
✔ déploiement simplifié  
✔ suivi complet via **MLflow**

### Suivi avec MLflow
- Log des métriques (Accuracy, AUC, etc.), paramètres et artefacts (plots SHAP)  
- Comparaison facile des versions  
- Traçabilité et reproductibilité  

Le modèle final est sauvegardé dans : `models/credit_scoring_model.pkl`

---

## API et Dashboard

- **API FastAPI** pour exposer le modèle  
- **Dashboard Streamlit** pour simuler les clients, afficher prédictions et explications SHAP  

### Exemple d’URL API Render :  
```text
https://credit-scoring-reg08-1.onrender.com/predict

## Configuration pour exécution locale

1 Cloner le dépôt :

 git clone <git@github.com:Bahmoud/credit-scoring-reg08.git>
cd Projet-ML-Credit-Scoring

2 Créer et activer un environnement Python :

python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

 3 Installer les dépendances :
 pip install -r requirements.txt

4 Lancer l’API :

uvicorn api.main:app --host 0.0.0.0 --port 8001

5 Lancer le dashboard :

streamlit run dashboard/app.py

