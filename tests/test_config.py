"""Tests pour le module de configuration"""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


class TestConfig:
    """Tests de la configuration"""

    def test_config_imports(self):
        """Test que la config peut être importée"""
        from config import DATA_PATH, TARGET, TEST_SIZE, RANDOM_STATE

        assert DATA_PATH is not None
        assert TARGET is not None
        assert TEST_SIZE is not None
        assert RANDOM_STATE is not None

    def test_test_size_valid(self):
        """Test que TEST_SIZE est valide"""
        from config import TEST_SIZE

        assert 0 < TEST_SIZE < 1, "TEST_SIZE doit être entre 0 et 1"

    def test_random_state_is_integer(self):
        """Test que RANDOM_STATE est un entier"""
        from config import RANDOM_STATE

        assert isinstance(RANDOM_STATE, int)
        assert RANDOM_STATE >= 0

    def test_target_is_string(self):
        """Test que TARGET est une chaîne"""
        from config import TARGET

        assert isinstance(TARGET, str)
        assert len(TARGET) > 0
