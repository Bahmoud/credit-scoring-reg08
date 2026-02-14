import mlflow
from sklearn.metrics import roc_auc_score, accuracy_score

def evaluate_model(model, X_test, y_test):

    pred = model.predict(X_test)
    prob = model.predict_proba(X_test)[:,1]

    acc = accuracy_score(y_test, pred)
    auc = roc_auc_score(y_test, prob)

    mlflow.log_metric("accuracy", acc)
    mlflow.log_metric("auc", auc)

    print("Accuracy:", acc)
    print("AUC:", auc)
