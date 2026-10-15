# Metodología

## Problema

Clasificación binaria de registros de vehículos entre `Privado` y `No_Privado`.

## Alcance

Se utilizaron vehículos con año de modelo 2016 o posterior.

## Preprocesamiento

El pipeline separa variables numéricas y categóricas y utiliza transformaciones compatibles con el entrenamiento de los modelos. Las variables categóricas de alta cardinalidad reciben un tratamiento específico para controlar la dimensionalidad de la representación.

## Modelos

Se evaluaron modelos de referencia y modelos supervisados, incluyendo Regresión Logística, Random Forest, Extra Trees, LightGBM y XGBoost.

## Evaluación

Debido al fuerte desbalance de clases, se utilizaron Precision, Recall, F1, ROC-AUC y PR-AUC, además de análisis mediante matriz de confusión y selección de threshold.

La selección operacional del threshold final se basa en probabilidades obtenidas mediante validación cruzada sobre entrenamiento, manteniendo el conjunto de prueba separado para la evaluación final.

## Explicabilidad y robustez

El modelo seleccionado se analizó mediante SHAP, estudio de ablación, análisis de errores y validación temporal.
