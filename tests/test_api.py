"""Tests pour l'API FastAPI"""
import pytest
from fastapi.testclient import TestClient
import sys
import os
from unittest.mock import patch, MagicMock
import joblib
import pandas as pd
import numpy as np

# Ajouter api au path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'api'))

from main import app

client = TestClient(app)


class TestAPIEndpoints:
    """Tests des endpoints de l'API"""

    def test_root_endpoint(self):
        """Test du endpoint racine"""
        response = client.get("/")

        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "projet" in data
        assert "Credit Scoring" in data["message"]

    @patch('api.utils.pipeline')
    @patch('api.utils.explainer')
    def test_predict_endpoint_valid_data(self, mock_explainer, mock_pipeline):
        """Test du endpoint de prédiction avec données valides"""
        # Mock du modèle
        mock_pipeline.predict_proba.return_value = np.array([[0.3, 0.7]])
        mock_pipeline.feature_names_in_ = ['age', 'income', 'loan_amount',
                                           'credit_history', 'employment_years']

        # Mock de l'explainer
        mock_explainer.shap_values.return_value = np.array([[0.1, 0.2, 0.3, 0.15, 0.05]])

        payload = {
            "age": 35,
            "income": 50000,
            "loan_amount": 25000,
            "credit_history": 10,
            "employment_years": 8
        }

        response = client.post("/predict", json=payload)

        assert response.status_code == 200
        data = response.json()

        assert "probabilite_defaut" in data
        assert "decision" in data
        assert "facteurs_principaux" in data

        assert 0 <= data["probabilite_defaut"] <= 1
        assert data["decision"] in ["ACCORDÉ", "REFUSÉ"]

    def test_predict_endpoint_missing_fields(self):
        """Test avec champs manquants"""
        payload = {
            "age": 35,
            "income": 50000
            # Champs manquants
        }

        response = client.post("/predict", json=payload)

        assert response.status_code == 422  # Validation error

    def test_predict_endpoint_invalid_types(self):
        """Test avec types invalides"""
        payload = {
            "age": "trente-cinq",  # String au lieu d'int
            "income": 50000,
            "loan_amount": 25000,
            "credit_history": 10,
            "employment_years": 8
        }

        response = client.post("/predict", json=payload)

        assert response.status_code == 422  # Validation error

    @patch('api.utils.pipeline')
    @patch('api.utils.explainer')
    def test_predict_endpoint_decision_logic(self, mock_explainer, mock_pipeline):
        """Test de la logique de décision"""
        mock_pipeline.feature_names_in_ = ['age', 'income', 'loan_amount',
                                           'credit_history', 'employment_years']
        mock_explainer.shap_values.return_value = np.array([[0.1, 0.2, 0.3, 0.15, 0.05]])

        payload = {
            "age": 35,
            "income": 50000,
            "loan_amount": 25000,
            "credit_history": 10,
            "employment_years": 8
        }

        # Test avec probabilité haute (>0.5) -> REFUSÉ
        mock_pipeline.predict_proba.return_value = np.array([[0.3, 0.7]])
        response = client.post("/predict", json=payload)
        assert response.json()["decision"] == "REFUSÉ"

        # Test avec probabilité basse (<0.5) -> ACCORDÉ
        mock_pipeline.predict_proba.return_value = np.array([[0.6, 0.4]])
        response = client.post("/predict", json=payload)
        assert response.json()["decision"] == "ACCORDÉ"


class TestAPISchema:
    """Tests du schéma de données"""

    def test_client_data_schema(self):
        """Test du schéma ClientData"""
        from schema import ClientData

        # Données valides
        valid_data = {
            "age": 35,
            "income": 50000,
            "loan_amount": 25000,
            "credit_history": 10,
            "employment_years": 8
        }

        client_data = ClientData(**valid_data)
        assert client_data.age == 35
        assert client_data.income == 50000

    def test_client_data_validation(self):
        """Test de validation du schéma"""
        from schema import ClientData
        from pydantic import ValidationError

        # Âge négatif
        with pytest.raises(ValidationError):
            ClientData(age=-5, income=50000, loan_amount=25000,
                      credit_history=10, employment_years=8)
