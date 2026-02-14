import shap
import mlflow
import matplotlib.pyplot as plt

def explain_model(model, X_sample):

    explainer = shap.Explainer(model.named_steps["model"])
    shap_values = explainer(X_sample)

    shap.plots.beeswarm(shap_values, show=False)
    plt.savefig("shap_summary.png")

    mlflow.log_artifact("shap_summary.png")
