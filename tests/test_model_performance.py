"""Tests de performance et qualité du modèle"""
import pytest
from unittest.mock import patch
import numpy as np
from sklearn.metrics import accuracy_score, roc_auc_score


class TestModelPerformance:
    """Tests de performance du modèle"""

    @patch('prepare.pd.read_csv')
    def test_model_minimum_accuracy(self, mock_read_csv, sample_data):
        """Test que le modèle atteint une précision minimale"""
        from prepare import load_data
        from train import train_model

        mock_read_csv.return_value = sample_data

        X_train, X_test, y_train, y_test = load_data()
        model = train_model(X_train, y_train)

        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)

        # Le modèle doit être meilleur qu'un classifieur aléatoire
        assert accuracy > 0.5, f"Accuracy {accuracy} trop basse"

    @patch('prepare.pd.read_csv')
    def test_model_roc_auc_score(self, mock_read_csv, sample_data):
        """Test du score ROC-AUC"""
        from prepare import load_data
        from train import train_model

        mock_read_csv.return_value = sample_data

        X_train, X_test, y_train, y_test = load_data()
        model = train_model(X_train, y_train)

        probas = model.predict_proba(X_test)[:, 1]

        # Vérifier que les deux classes sont présentes
        if len(np.unique(y_test)) == 2:
            roc_auc = roc_auc_score(y_test, probas)
            assert roc_auc > 0.5, f"ROC-AUC {roc_auc} trop bas"

    @patch('prepare.pd.read_csv')
    def test_model_not_overfitting(self, mock_read_csv, sample_data):
        """Test que le modèle ne sur-apprend pas"""
        from prepare import load_data
        from train import train_model

        mock_read_csv.return_value = sample_data

        X_train, X_test, y_train, y_test = load_data()
        model = train_model(X_train, y_train)

        # Précision sur train et test
        train_accuracy = accuracy_score(y_train, model.predict(X_train))
        test_accuracy = accuracy_score(y_test, model.predict(X_test))

        # La différence ne doit pas être trop grande (> 20%)
        accuracy_diff = train_accuracy - test_accuracy
        assert accuracy_diff < 0.2, f"Possible overfitting: diff={accuracy_diff}"

    @patch('prepare.pd.read_csv')
    def test_prediction_probability_range(self, mock_read_csv, sample_data):
        """Test que les probabilités sont dans [0, 1]"""
        from prepare import load_data
        from train import train_model

        mock_read_csv.return_value = sample_data

        X_train, X_test, y_train, y_test = load_data()
        model = train_model(X_train, y_train)

        probas = model.predict_proba(X_test)

        assert np.all(probas >= 0)
        assert np.all(probas <= 1)
        assert np.allclose(probas.sum(axis=1), 1.0)

    @patch('prepare.pd.read_csv')
    def test_prediction_consistency(self, mock_read_csv, sample_data):
        """Test de la cohérence des prédictions"""
        from prepare import load_data
        from train import train_model

        mock_read_csv.return_value = sample_data

        X_train, X_test, y_train, y_test = load_data()
        model = train_model(X_train, y_train)

        # Prédire plusieurs fois sur les mêmes données
        pred1 = model.predict(X_test)
        pred2 = model.predict(X_test)
        pred3 = model.predict(X_test)

        # Les prédictions doivent être identiques
        np.testing.assert_array_equal(pred1, pred2)
        np.testing.assert_array_equal(pred2, pred3)


class TestModelRobustness:
    """Tests de robustesse du modèle"""

    @patch('prepare.pd.read_csv')
    def test_model_handles_edge_cases(self, mock_read_csv, sample_data):
        """Test que le modèle gère les cas limites"""
        from prepare import load_data
        from train import train_model
        import pandas as pd

        mock_read_csv.return_value = sample_data

        X_train, X_test, y_train, y_test = load_data()
        model = train_model(X_train, y_train)

        # Créer des données avec valeurs extrêmes
        edge_case = pd.DataFrame({
            col: [X_train[col].min(), X_train[col].max()]
            for col in X_train.columns
        })

        # Ne devrait pas planter
        predictions = model.predict(edge_case)
        assert len(predictions) == 2

    @patch('prepare.pd.read_csv')
    def test_model_prediction_speed(self, mock_read_csv, sample_data):
        """Test de la vitesse de prédiction"""
        from prepare import load_data
        from train import train_model
        import time

        mock_read_csv.return_value = sample_data

        X_train, X_test, y_train, y_test = load_data()
        model = train_model(X_train, y_train)

        # Mesurer le temps de prédiction
        start = time.time()
        model.predict(X_test)
        elapsed = time.time() - start

        # La prédiction doit être rapide (< 1 seconde pour 100 samples)
        assert elapsed < 1.0, f"Prédiction trop lente: {elapsed}s"
