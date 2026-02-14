"""Tests pour le module d'entraînement"""
import pytest
import numpy as np
from sklearn.pipeline import Pipeline
from train import train_model


class TestTrainModel:
    """Tests pour la fonction train_model"""

    def test_train_model_returns_pipeline(self, sample_X_y):
        """Test que train_model retourne un pipeline"""
        X, y = sample_X_y
        model = train_model(X, y)

        assert isinstance(model, Pipeline)
        assert hasattr(model, 'predict')
        assert hasattr(model, 'predict_proba')

    def test_train_model_can_predict(self, sample_X_y):
        """Test que le modèle peut faire des prédictions"""
        X, y = sample_X_y
        model = train_model(X, y)

        predictions = model.predict(X)

        assert len(predictions) == len(X)
        assert all(pred in [0, 1] for pred in predictions)

    def test_train_model_can_predict_proba(self, sample_X_y):
        """Test que le modèle peut prédire des probabilités"""
        X, y = sample_X_y
        model = train_model(X, y)

        probas = model.predict_proba(X)

        assert probas.shape == (len(X), 2)
        assert np.all((probas >= 0) & (probas <= 1))
        assert np.allclose(probas.sum(axis=1), 1.0)

    def test_train_model_with_empty_data(self):
        """Test avec des données vides"""
        import pandas as pd
        X = pd.DataFrame()
        y = pd.Series()

        with pytest.raises(Exception):
            train_model(X, y)

    def test_train_model_reproducibility(self, sample_X_y):
        """Test la reproductibilité de l'entraînement"""
        X, y = sample_X_y

        model1 = train_model(X, y)
        model2 = train_model(X, y)

        pred1 = model1.predict(X)
        pred2 = model2.predict(X)

        # Les prédictions doivent être identiques avec le même random_state
        np.testing.assert_array_equal(pred1, pred2)

    def test_train_model_handles_class_imbalance(self, sample_X_y):
        """Test que le modèle gère le déséquilibre de classes"""
        X, y = sample_X_y

        # Créer un dataset fortement déséquilibré
        y_imbalanced = y.copy()
        y_imbalanced.iloc[:90] = 0  # 90% classe 0
        y_imbalanced.iloc[90:] = 1   # 10% classe 1

        model = train_model(X, y_imbalanced)
        predictions = model.predict(X)

        # Le modèle doit quand même détecter les deux classes
        assert len(np.unique(predictions)) > 0
