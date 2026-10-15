"""Utilidades SHAP optativas.

La explicación SHAP puede consumir bastante memoria/tiempo. Esta función no se
ejecuta automáticamente y trabaja sobre una muestra que el usuario proporciona.
"""
def explain_random_forest_pipeline(model, X_sample):
    """Calcula SHAP para la clase positiva usando una muestra explícita.

    `model` debe ser el Pipeline entrenado con pasos `preprocessor` y `model`.
    La salida exacta de SHAP puede variar según su versión; inspecciona
    `shap_values` antes de asumir una forma concreta.
    """
    import shap

    X_transformed = model.named_steps["preprocessor"].transform(X_sample)
    estimator = model.named_steps["model"]
    explainer = shap.TreeExplainer(estimator)
    shap_values = explainer.shap_values(X_transformed)
    return explainer, shap_values, X_transformed
