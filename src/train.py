from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier
from config import N_ESTIMATORS, RANDOM_STATE

def train_model(X_train, y_train):
    pipeline = Pipeline([
        ("imputer", SimpleImputer()),
        ("scaler", StandardScaler()),
        ("model", GradientBoostingClassifier(
            n_estimators=N_ESTIMATORS,
            random_state=RANDOM_STATE
        ))
    ])

    pipeline.fit(X_train, y_train)
    return pipeline
