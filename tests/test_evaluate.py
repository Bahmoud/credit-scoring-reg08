"""Tests pour le module d'évaluation"""
import pytest
from unittest.mock import patch, MagicMock
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from evaluate import evaluate_model


class TestEvaluateModel:
    """Tests pour la fonction evaluate_model"""

    def test_evaluate_model_runs_without_error(self, sample_X_y):
        """Test que evaluate_model s'exécute sans erreur"""
        X, y = sample_X_y

        # Créer un modèle simple
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.preprocessing import StandardScaler

        model = Pipeline([
            ('scaler', StandardScaler()),
            ('classifier', RandomForestClassifier(n_estimators=10, random_state=42))
        ])
        model.fit(X, y)

        # Ne devrait pas lever d'exception
        try:
            evaluate_model(model, X, y)
            success = True
        except Exception:
            success = False

        assert success

    @patch('evaluate.mlflow.log_metric')
    def test_evaluate_model_logs_metrics(self, mock_log_metric, sample_X_y):
        """Test que les métriques sont loguées"""
        X, y = sample_X_y

        from sklearn.ensemble import RandomForestClassifier
        from sklearn.preprocessing import StandardScaler

        model = Pipeline([
            ('scaler', StandardScaler()),
            ('classifier', RandomForestClassifier(n_estimators=10, random_state=42))
        ])
        model.fit(X, y)

        evaluate_model(model, X, y)

        # Vérifier que mlflow.log_metric a été appelé
        assert mock_log_metric.called

    def test_evaluate_model_with_perfect_predictions(self, sample_X_y):
        """Test avec des prédictions parfaites"""
        X, y = sample_X_y

        # Mock d'un modèle qui prédit toujours correctement
        mock_model = MagicMock()
        mock_model.predict.return_value = y
        mock_model.predict_proba.return_value = np.column_stack([1 - y, y])

        # Ne devrait pas lever d'exception
        evaluate_model(mock_model, X, y)

    def test_evaluate_model_with_poor_predictions(self, sample_X_y):
        """Test avec de mauvaises prédictions"""
        X, y = sample_X_y

        # Mock d'un modèle qui prédit toujours la classe opposée
        mock_model = MagicMock()
        mock_model.predict.return_value = 1 - y
        mock_model.predict_proba.return_value = np.column_stack([y, 1 - y])

        # Ne devrait pas lever d'exception même avec de mauvais résultats
        evaluate_model(mock_model, X, y)
