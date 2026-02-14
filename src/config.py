from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "data_fe.csv"

TARGET = "TARGET"  # remplacer par la vraie colonne cible du CSV
TEST_SIZE = 0.2
RANDOM_STATE = 42
N_ESTIMATORS = 100
