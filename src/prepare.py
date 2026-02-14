import pandas as pd
from sklearn.model_selection import train_test_split
from config import DATA_PATH, TARGET, TEST_SIZE, RANDOM_STATE

def load_data():
    df = pd.read_csv(DATA_PATH)
    
    # Vérifie que la colonne cible existe
    if TARGET not in df.columns:
        raise ValueError(f"La colonne cible '{TARGET}' n'existe pas dans le dataset. Colonnes trouvées : {df.columns.tolist()}")

    X = df.drop(TARGET, axis=1)
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE
    )
    return X_train, X_test, y_train, y_test
