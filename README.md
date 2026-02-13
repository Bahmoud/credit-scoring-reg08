# Credit Scoring Machine Learning — Projet REG08

##  Objectif du projet
Ce projet vise à construire un système de **scoring de crédit automatisé** capable de :

- estimer la probabilité de défaut d’un client
- aider à la décision d’octroi de crédit
- expliquer la décision du modèle (interprétabilité)
- proposer une interface utilisateur simple
- exposer le modèle via une API

Le projet suit une démarche complète de Data Science et MLOps.

---

##  Problème métier

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

##  Jeux de données utilisés

Les données proviennent du projet **Home Credit Default Risk**.

### 1️ application_train
Informations principales sur les clients :
- caractéristiques personnelles
- informations financières
- informations de crédit

➡ Dataset principal du modèle.

---

### 2️ bureau
Historique de crédits du client auprès d’autres institutions.

Exemples d’informations :
- crédits passés
- statut des crédits
- montants empruntés

➡ Permet d’évaluer le comportement financier historique.

---

### 3️ bureau_balance
Historique mensuel des crédits du dataset bureau.

➡ Permet d’observer l’évolution du comportement de remboursement dans le temps.

---

### 4️ previous_application
Historique des anciennes demandes de crédit du client.

➡ Permet d’évaluer l’expérience passée avec les prêts.

---

## Feature Engineering

Les étapes réalisées :

✔ fusion des datasets  
✔ création de variables agrégées  
✔ gestion des valeurs manquantes  
✔ encodage des variables catégorielles  
✔ normalisation si nécessaire  

Exemple :
- agrégation de l’historique de crédit
- création d’indicateurs de stabilité financière
- création de variables de comportement client

---

## Modélisation

### Modèles testés
Plusieurs modèles ont été évalués pour comparer les performances.

Le modèle retenu est :

 Gradient Boosting

Pourquoi ce choix :
- bonnes performances sur données tabulaires
- gestion des relations non linéaires
- robuste aux variables nombreuses
- bon compromis biais / variance

---

## Pipeline Machine Learning

Le projet utilise un pipeline complet :

Prétraitement → Transformation → Modèle → Prédiction

Avantages :
✔ reproductibilité  
✔ cohérence entre entraînement et prédiction  
✔ déploiement simplifié  

Le pipeline final est sauvegardé dans :

model/credit_scoring_model.pkl

-----

##  Interprétabilité du modèle (Explainable AI)

Le projet intègre un mécanisme d’explication des décisions du modèle.

Nous utilisons la méthode SHAP (Shapley Additive Explanations), qui permet de :

✔ identifier les variables qui influencent la décision  
✔ mesurer l’impact de chaque variable  
✔ expliquer individuellement chaque prédiction  
✔ rendre la décision compréhensible pour un utilisateur non technique  

L’API retourne :
- la probabilité de défaut
- la décision de crédit
- les principaux facteurs explicatifs

Ces explications sont affichées directement dans le dashboard utilisateur sous forme de facteurs qui :
- augmentent le risque  
- réduisent le risque  

Cette approche permet de rendre le système de scoring transparent et interprétable.


