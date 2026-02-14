import sys
import os

# 🔹 Ajouter le dossier src au Python path
sys.path.append(os.path.join(os.getcwd(), "src"))

# 🔹 Importer tous les modules du pipeline
from prepare import load_data
from train import train_model
from evaluate import evaluate_model
from explain import explain_model

def test_pipeline():
    print("=== Chargement des données ===")
    X_train, X_test, y_train, y_test = load_data()
    print("X_train shape:", X_train.shape)
    print("X_test shape:", X_test.shape)

    print("\n=== Entraînement du modèle ===")
    model = train_model(X_train, y_train)
    print("Pipeline entraîné :", model)

    print("\n=== Évaluation ===")
    evaluate_model(model, X_test, y_test)

    print("\n=== Explication SHAP (100 premières instances) ===")
    explain_model(model, X_test[:100])
    print("Graphique shap_beeswarm.png créé avec succès !")

if __name__ == "__main__":
    test_pipeline()
