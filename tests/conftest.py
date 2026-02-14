"""Configuration pytest et fixtures communes"""
import pytest
import pandas as pd
import numpy as np
import sys
import os

# Ajouter src au path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'api'))


@pytest.fixture
def sample_data():
    """Données de test factices correspondant au schéma réel"""
    np.random.seed(42)
    n_samples = 100

    data = {
        'EXT_SOURCE_1': np.random.uniform(0, 1, n_samples),
        'EXT_SOURCE_2': np.random.uniform(0, 1, n_samples),
        'EXT_SOURCE_3': np.random.uniform(0, 1, n_samples),
        'AMT_GOODS_PRICE': np.random.uniform(50000, 1000000, n_samples),
        'AMT_ANNUITY': np.random.uniform(5000, 100000, n_samples),
        'AMT_CREDIT': np.random.uniform(50000, 1000000, n_samples),
        'DAYS_BIRTH': np.random.randint(-25000, -7000, n_samples).astype(float),
        'DAYS_EMPLOYED': np.random.randint(-15000, 0, n_samples).astype(float),
        'DAYS_LAST_PHONE_CHANGE': np.random.randint(-4000, 0, n_samples).astype(float),
        'NAME_FAMILY_STATUS_Married': np.random.randint(0, 2, n_samples),
        'REGION_RATING_CLIENT': np.random.randint(1, 4, n_samples).astype(float),
        'REGION_RATING_CLIENT_W_CITY': np.random.randint(1, 4, n_samples).astype(float),
        'FLAG_DOCUMENT_3': np.random.randint(0, 2, n_samples),
        'DAYS_ID_PUBLISH': np.random.randint(-7000, 0, n_samples).astype(float),
        'OCCUPATION_TYPE_Laborers': np.random.randint(0, 2, n_samples),
        'TARGET': np.random.randint(0, 2, n_samples)
    }

    return pd.DataFrame(data)


@pytest.fixture
def sample_X_y(sample_data):
    """Features et target séparés"""
    X = sample_data.drop('TARGET', axis=1)
    y = sample_data['TARGET']
    return X, y


@pytest.fixture
def client_data_valid():
    """Données client valides pour l'API"""
    return {
        "EXT_SOURCE_1": 0.5,
        "EXT_SOURCE_2": 0.6,
        "EXT_SOURCE_3": 0.4,
        "AMT_GOODS_PRICE": 500000.0,
        "AMT_ANNUITY": 25000.0,
        "AMT_CREDIT": 600000.0,
        "DAYS_BIRTH": -12000.0,
        "DAYS_EMPLOYED": -2000.0,
        "DAYS_LAST_PHONE_CHANGE": -1000.0,
        "NAME_FAMILY_STATUS_Married": 1,
        "REGION_RATING_CLIENT": 2.0,
        "REGION_RATING_CLIENT_W_CITY": 2.0,
        "FLAG_DOCUMENT_3": 1,
        "DAYS_ID_PUBLISH": -3000.0,
        "OCCUPATION_TYPE_Laborers": 0
    }


@pytest.fixture
def client_data_invalid():
    """Données client invalides"""
    return {
        "EXT_SOURCE_1": 0.5,
        "EXT_SOURCE_2": 0.6
        # Champs manquants
    }
