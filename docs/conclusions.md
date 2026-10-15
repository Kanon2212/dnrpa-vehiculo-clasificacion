# Conclusiones

El proyecto muestra que es posible obtener capacidad de discriminación para identificar registros `No_Privado` a pesar del fuerte desbalance de clases.

XGBoost obtuvo el mejor comportamiento de ranking global, mientras que Random Forest presentó el mejor equilibrio operacional observado con el threshold seleccionado y fue utilizado como modelo principal para el análisis de explicabilidad y robustez.

El análisis SHAP, la ablación y el estudio de errores permiten identificar la importancia de las características del vehículo y otras variables administrativas, del titular y de localización.

La validación temporal muestra un deterioro importante del desempeño operacional respecto de la validación aleatoria. Por ello, el modelo no debería considerarse listo para producción sin validación temporal adicional, monitoreo y recalibración del threshold.
