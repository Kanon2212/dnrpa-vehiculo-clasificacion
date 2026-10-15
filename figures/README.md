# Figures
Este directorio contiene visualizaciones listas para su inclusión en un portafolio, generadas a partir de los resultados cuantitativos validados del *notebook* ejecutado.

## Nota importante

Las curvas ROC y de precisión-exhaustividad (*precision-recall*) no se generan únicamente a partir de métricas resumidas; requieren las probabilidades de predicción originales. Por ello, este primer conjunto de figuras incluye deliberadamente solo aquellas visualizaciones que pueden reproducirse directamente a partir de las tablas de resultados consolidados, sin necesidad de reconstruir ni reentrenar modelos.

## Secciones

- `model/`: comparación final de modelos.
- `threshold/`: sensibilidad del umbral de referencia (Random Forest).
- `ablation/`: estudio de ablación de grupos de características.
- `errors/`: resumen de errores.
- `temporal/`: validación temporal.
- `shap/`: patrones SHAP en los falsos negativos.
