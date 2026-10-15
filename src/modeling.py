"""Construcción e inferencia del Random Forest del proyecto."""
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

from .preprocessing import build_preprocessor

POSITIVE_CLASS = "No_Privado"
NEGATIVE_CLASS = "Privado"
DECISION_THRESHOLD = 0.31


def build_random_forest_pipeline():
    """Construye el pipeline con los hiperparámetros finales documentados.

    Esta función crea el estimador, pero no lo entrena. El entrenamiento debe
    hacerse explícitamente con los datos de entrenamiento autorizados.
    """
    classifier = RandomForestClassifier(
        n_estimators=200,
        max_depth=None,
        min_samples_split=5,
        min_samples_leaf=1,
        max_features="log2",
        class_weight="balanced",
        criterion="gini",
        bootstrap=True,
        max_samples=None,
        random_state=42,
        n_jobs=-1,
    )
    return Pipeline([
        ("preprocessor", build_preprocessor()),
        ("model", classifier),
    ])


def predict_no_privado(model, X, threshold=DECISION_THRESHOLD):
    """Devuelve probabilidades y predicciones binarias para No_Privado.

    Requiere que el pipeline se haya entrenado con etiquetas binarias:
    1 = No_Privado y 0 = Privado.
    """
    probabilities = model.predict_proba(X)[:, 1]
    predictions = (probabilities >= threshold).astype(int)
    return probabilities, predictions
