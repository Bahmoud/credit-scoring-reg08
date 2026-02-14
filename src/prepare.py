import pandas as pd
from sklearn.model_selection import train_test_split
from config import DATA_PATH, TARGET, TEST_SIZE, RANDOM_STATE

def load_data():
    df = pd.read_csv(DATA_PATH)

    X = df.drop(TARGET, axis=1)
    y = df[TARGET]

    return train_test_split(
        X, y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE
    )
