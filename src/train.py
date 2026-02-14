import mlflow
import mlflow.sklearn

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

from config import N_ESTIMATORS, RANDOM_STATE

def build_model():

    pipe = Pipeline([
        ("imputer", SimpleImputer()),
        ("scaler", StandardScaler()),
        ("model", RandomForestClassifier(
            n_estimators=N_ESTIMATORS,
            random_state=RANDOM_STATE
        ))
    ])

    return pipe


def train_model(X_train, y_train):

    model = build_model()

    mlflow.log_param("model", "RandomForest")
    mlflow.log_param("n_estimators", N_ESTIMATORS)

    model.fit(X_train, y_train)

    mlflow.sklearn.log_model(model, "model")

    return model
