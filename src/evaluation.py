"""Métricas para la clase positiva No_Privado."""
import numpy as np
from sklearn.metrics import (
    average_precision_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)


def evaluate_binary_classifier(y_true, probabilities, threshold=0.31):
    """Calcula métricas de ranking y métricas dependientes del umbral.

    y_true debe estar codificado como 1=No_Privado y 0=Privado.
    """
    y_true = np.asarray(y_true)
    probabilities = np.asarray(probabilities)
    predictions = (probabilities >= threshold).astype(int)
    tn, fp, fn, tp = confusion_matrix(y_true, predictions, labels=[0, 1]).ravel()

    return {
        "threshold": float(threshold),
        "TN": int(tn),
        "FP": int(fp),
        "FN": int(fn),
        "TP": int(tp),
        "precision_no_privado": float(precision_score(y_true, predictions, zero_division=0)),
        "recall_no_privado": float(recall_score(y_true, predictions, zero_division=0)),
        "f1_no_privado": float(f1_score(y_true, predictions, zero_division=0)),
        "roc_auc": float(roc_auc_score(y_true, probabilities)),
        "pr_auc_average_precision": float(average_precision_score(y_true, probabilities)),
    }
