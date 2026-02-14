"""Tests pour le module de préparation des données"""
import pytest
import pandas as pd
import numpy as np
from unittest.mock import patch, MagicMock
from prepare import load_data


class TestLoadData:
    """Tests pour la fonction load_data"""

    @patch('prepare.pd.read_csv')
    def test_load_data_success(self, mock_read_csv, sample_data):
        """Test du chargement réussi des données"""
        mock_read_csv.return_value = sample_data

        X_train, X_test, y_train, y_test = load_data()

        # Vérifier les types
        assert isinstance(X_train, pd.DataFrame)
        assert isinstance(X_test, pd.DataFrame)
        assert isinstance(y_train, pd.Series)
        assert isinstance(y_test, pd.Series)

        # Vérifier les dimensions
        assert X_train.shape[0] + X_test.shape[0] == len(sample_data)
        assert len(y_train) == X_train.shape[0]
        assert len(y_test) == X_test.shape[0]

        # Vérifier qu'il n'y a pas de colonne target dans X
        assert 'default' not in X_train.columns
        assert 'default' not in X_test.columns

    @patch('prepare.pd.read_csv')
    def test_load_data_missing_target(self, mock_read_csv, sample_data):
        """Test avec colonne cible manquante"""
        # Créer un DataFrame sans la colonne target
        df_no_target = sample_data.drop('TARGET', axis=1)
        mock_read_csv.return_value = df_no_target

        with pytest.raises(ValueError, match="La colonne cible"):
            load_data()

    @patch('prepare.pd.read_csv')
    def test_load_data_split_ratio(self, mock_read_csv, sample_data):
        """Test du ratio de split"""
        mock_read_csv.return_value = sample_data

        X_train, X_test, y_train, y_test = load_data()

        # Vérifier approximativement le ratio 80/20
        total = len(X_train) + len(X_test)
        test_ratio = len(X_test) / total
        assert 0.15 < test_ratio < 0.25  # Tolérance autour de 0.2

    @patch('prepare.pd.read_csv')
    def test_load_data_no_data_leakage(self, mock_read_csv, sample_data):
        """Test qu'il n'y a pas de fuite de données entre train et test"""
        mock_read_csv.return_value = sample_data

        X_train, X_test, y_train, y_test = load_data()

        # Vérifier qu'aucune ligne de test n'apparaît dans train
        # (En utilisant l'index comme identifiant)
        train_indices = set(X_train.index)
        test_indices = set(X_test.index)

        assert len(train_indices.intersection(test_indices)) == 0
