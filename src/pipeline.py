import mlflow
import os
import joblib
from prepare import load_data
from train import train_model
from evaluate import evaluate_model
from explain import explain_model

def run_pipeline():
    with mlflow.start_run(run_name="credit_pipeline"):

        # ======================
        # 1️ Charger les données
        # ======================
        X_train, X_test, y_train, y_test = load_data()
        print(f"X_train shape: {X_train.shape}, X_test shape: {X_test.shape}")

        # ======================
        # 2️ Entraîner le modèle
        # ======================
        model = train_model(X_train, y_train)
        print("Pipeline entraîné :", model)

        # ======================
        # 3️ Évaluer le modèle
        # ======================
        evaluate_model(model, X_test, y_test)

        # ======================
        # 4️ Expliquer le modèle avec SHAP sur 100 instances
        # ======================
        explain_model(model, X_test[:100])

        # ======================
        # 5️ Sauvegarder le modèle pour l’API
        # ======================
        os.makedirs("models", exist_ok=True)
        joblib.dump(model, "models/credit_scoring_model.pkl")
        print("Modèle sauvegardé dans models/credit_scoring_model.pkl")

if __name__ == "__main__":
    run_pipeline()
