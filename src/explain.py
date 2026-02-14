import shap
import matplotlib.pyplot as plt
import pandas as pd

def explain_model(pipeline, X_sample: pd.DataFrame):
    """
    Explique le modèle Pipeline avec SHAP et sauvegarde un graphique beeswarm.
    Compatible GradientBoosting / RandomForest et classification binaire.
    """

    # Récupérer le modèle final
    model = pipeline.named_steps['model']

    # Appliquer le prétraitement du pipeline si présent
    if len(pipeline.steps) > 1:
        X_transformed = pipeline[:-1].transform(X_sample)
    else:
        X_transformed = X_sample

    # TreeExplainer
    explainer = shap.TreeExplainer(model, model_output="raw")
    shap_values_all = explainer(X_transformed)

    # Sélectionner la classe positive si classification binaire
    if isinstance(shap_values_all, list):
        shap_values_array = shap_values_all[1]
    else:
        shap_values_array = shap_values_all.values

    # Transformer en Explanation object compatible beeswarm
    shap_values = shap.Explanation(
        values=shap_values_array,
        data=X_transformed,
        feature_names=X_sample.columns
    )

    # Tracer le beeswarm
    shap.plots.beeswarm(shap_values, show=False)

    # Sauvegarder le graphique
    plt.savefig("shap_beeswarm.png")
    plt.close()
