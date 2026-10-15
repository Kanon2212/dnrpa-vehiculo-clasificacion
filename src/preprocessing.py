"""Preprocesamiento de variables para el proyecto DNRPA.

Implementa la misma estrategia documentada en el notebook:
- imputación por mediana y escalado para variables numéricas;
- imputación por moda y OneHotEncoder para variables categóricas;
- min_frequency=5 para categorías de baja/media cardinalidad;
- min_frequency=10 para categorías de alta cardinalidad.
"""
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

NUMERIC_FEATURES = [
    "automotor_anio_modelo",
    "titular_anio_nacimiento",
    "titular_porcentaje_titularidad",
    "antiguedad_vehiculo",
    "tramite_anio",
    "tramite_mes",
    "inscripcion_anio",
    "inscripcion_mes",
]

CATEGORICAL_LOW_MEDIUM = [
    "tramite_tipo",
    "registro_seccional_provincia",
    "automotor_origen",
    "automotor_tipo_descripcion",
    "automotor_marca_descripcion",
    "titular_tipo_persona",
    "titular_domicilio_provincia",
    "titular_genero",
    "titular_pais_nacimiento",
]

CATEGORICAL_HIGH = [
    "automotor_modelo_descripcion",
    "titular_domicilio_localidad",
]

FEATURES = NUMERIC_FEATURES + CATEGORICAL_LOW_MEDIUM + CATEGORICAL_HIGH


def build_preprocessor():
    """Construye y devuelve el ColumnTransformer del notebook."""
    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])

    categorical_low_medium_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore", min_frequency=5)),
    ])

    categorical_high_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore", min_frequency=10)),
    ])

    return ColumnTransformer([
        ("num", numeric_pipeline, NUMERIC_FEATURES),
        ("cat_low_medium", categorical_low_medium_pipeline, CATEGORICAL_LOW_MEDIUM),
        ("cat_high", categorical_high_pipeline, CATEGORICAL_HIGH),
    ])


def validate_feature_columns(X):
    """Comprueba que estén presentes las 19 variables predictoras esperadas."""
    missing = [column for column in FEATURES if column not in X.columns]
    extra = [column for column in X.columns if column not in FEATURES]
    if missing or extra:
        raise ValueError(
            f"Esquema de variables inesperado. Faltantes={missing}; adicionales={extra}"
        )
    return X[FEATURES].copy()
