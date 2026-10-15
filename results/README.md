# Results
Este directorio contiene los principales resultados cuantitativos del proyecto de clasificación de vehículos de la DNRPA.

## Distinción metodológica importante

El **modelo final** es el modelo *Random Forest* optimizado (*tuned*), evaluado con un umbral de **0,31** seleccionado mediante validación *out-of-fold* (OOF).

El modelo *Random Forest* con un umbral de **0,35** es el **RF de referencia** (*baseline*) utilizado para:
- el análisis SHAP
- el estudio de ablación
- el análisis detallado de errores
- la validación temporal

Estos análisis se conservan tal como aparecen en el *notebook* ejecutado y no se presentan como una reevaluación del RF optimizado.

## Archivos

- `metrics/model_comparison.csv`: comparación de modelos finales.
- `metrics/rf_reference_threshold_analysis.csv`: análisis de sensibilidad al umbral del RF de referencia.
- `ablation/ablation_results.csv`: resultados de ablación por grupos de características (*feature groups*).
- `errors/error_summary.csv`: resumen de probabilidades de TN, FP, FN y TP.
- `temporal/temporal_comparison.csv`: resultados de la validación temporal.
- `shap/fn_shap_patterns.csv`: patrones SHAP observados en los falsos negativos.

Los valores corresponden a los resultados del *notebook* ejecutado.