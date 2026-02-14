import mlflow
from prepare import load_data
from train import train_model
from evaluate import evaluate_model
from explain import explain_model

def run_pipeline():

    with mlflow.start_run(run_name="credit_pipeline"):

        X_train, X_test, y_train, y_test = load_data()

        model = train_model(X_train, y_train)

        evaluate_model(model, X_test, y_test)

        explain_model(model, X_test[:100])


if __name__ == "__main__":
    run_pipeline()
