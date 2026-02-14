"""Tests d'intégration du pipeline complet"""
import pytest
import os
import sys
from unittest.mock import patch
import pandas as pd
import joblib

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from prepare import load_data
from train import train_model
from evaluate import evaluate_model


class TestPipelineIntegration:
    """Tests d'intégration du pipeline ML"""

    @patch('prepare.pd.read_csv')
    def test_full_pipeline_execution(self, mock_read_csv, sample_data):
        """Test de l'exécution complète du pipeline"""
        mock_read_csv.return_value = sample_data

        # 1. Charger les données
        X_train, X_test, y_train, y_test = load_data()
        assert X_train is not None
        assert X_test is not None

        # 2. Entraîner le modèle
        model = train_model(X_train, y_train)
        assert model is not None

        # 3. Évaluer le modèle
        evaluate_model(model, X_test, y_test)

        # 4. Prédire sur de nouvelles données
        predictions = model.predict(X_test)
        assert len(predictions) == len(X_test)

    @patch('prepare.pd.read_csv')
    def test_model_persistence(self, mock_read_csv, sample_data, tmp_path):
        """Test de la sauvegarde et du chargement du modèle"""
        mock_read_csv.return_value = sample_data

        # Entraîner le modèle
        X_train, X_test, y_train, y_test = load_data()
        model = train_model(X_train, y_train)

        # Sauvegarder
        model_path = tmp_path / "test_model.pkl"
        joblib.dump(model, model_path)

        # Charger
        loaded_model = joblib.load(model_path)

        # Vérifier que les prédictions sont identiques
        original_preds = model.predict(X_test)
        loaded_preds = loaded_model.predict(X_test)

        import numpy as np
        np.testing.assert_array_equal(original_preds, loaded_preds)

    @patch('prepare.pd.read_csv')
    def test_pipeline_reproducibility(self, mock_read_csv, sample_data):
        """Test de la reproductibilité du pipeline"""
        mock_read_csv.return_value = sample_data

        # Première exécution
        X_train1, X_test1, y_train1, y_test1 = load_data()
        model1 = train_model(X_train1, y_train1)
        preds1 = model1.predict(X_test1)

        # Deuxième exécution
        X_train2, X_test2, y_train2, y_test2 = load_data()
        model2 = train_model(X_train2, y_train2)
        preds2 = model2.predict(X_test2)

        # Les résultats doivent être identiques
        import numpy as np
        np.testing.assert_array_equal(preds1, preds2)

    @patch('prepare.pd.read_csv')
    def test_end_to_end_with_api_format(self, mock_read_csv, sample_data):
        """Test end-to-end avec format de données API"""
        mock_read_csv.return_value = sample_data

        # Entraîner le modèle
        X_train, X_test, y_train, y_test = load_data()
        model = train_model(X_train, y_train)

        # Simuler une requête API
        client_data = {
            "age": 35,
            "income": 50000,
            "loan_amount": 25000,
            "credit_history": 10,
            "employment_years": 8
        }

        df = pd.DataFrame([client_data])
        df = df.reindex(columns=model.feature_names_in_, fill_value=0)

        # Prédire
        proba = model.predict_proba(df)[0, 1]

        assert 0 <= proba <= 1
        assert isinstance(proba, float)


class TestDataQuality:
    """Tests de qualité des données"""

    @patch('prepare.pd.read_csv')
    def test_no_missing_values_after_split(self, mock_read_csv, sample_data):
        """Test qu'il n'y a pas de valeurs manquantes après le split"""
        mock_read_csv.return_value = sample_data

        X_train, X_test, y_train, y_test = load_data()

        assert not X_train.isnull().any().any()
        assert not X_test.isnull().any().any()
        assert not y_train.isnull().any()
        assert not y_test.isnull().any()

    @patch('prepare.pd.read_csv')
    def test_feature_types_consistency(self, mock_read_csv, sample_data):
        """Test de la cohérence des types de features"""
        mock_read_csv.return_value = sample_data

        X_train, X_test, y_train, y_test = load_data()

        # Les types doivent être identiques entre train et test
        assert X_train.dtypes.equals(X_test.dtypes)

    @patch('prepare.pd.read_csv')
    def test_target_distribution(self, mock_read_csv, sample_data):
        """Test de la distribution de la variable cible"""
        mock_read_csv.return_value = sample_data

        X_train, X_test, y_train, y_test = load_data()

        # La cible doit contenir au moins 2 classes
        assert len(y_train.unique()) >= 2
        assert len(y_test.unique()) >= 1

        # Les classes doivent être binaires (0, 1)
        if len(y_train.unique()) > 0:
            assert set(y_train.unique()).issubset({0, 1})
        if len(y_test.unique()) > 0:
            assert set(y_test.unique()).issubset({0, 1})
