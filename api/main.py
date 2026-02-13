from fastapi import FastAPI
from api.schema import ClientData
from api.utils import predict_client


# Création de l'application
app = FastAPI(
    title="API Credit Scoring",
    description="Prédiction du risque de défaut client",
    version="1.0"
)

# Route de test
@app.get("/")
def root():
    return {
        "message": "API Credit Scoring opérationnelle",
        "projet": "REG08 - Credit Scoring ML"
    }

# Endpoint de prédiction
@app.post("/predict")
def predict(data: ClientData):
    """
    Prédiction du risque client
    Entrée : données client
    Sortie : score + décision + explication
    """
    result = predict_client(data.dict())
    return result
