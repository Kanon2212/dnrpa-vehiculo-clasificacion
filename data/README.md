# Datos

Este directorio no incluye el dataset original ni copias de registros individuales.

## Dataset del proyecto

El proyecto trabaja con registros de automotores de la DNRPA y utiliza un subconjunto filtrado por año-modelo:

- Filtro aplicado: `automotor_anio_modelo >= 2016`.
- Tamaño documentado del dataset de modelado: 62.310 filas.
- Variables predictoras: 19.
- Variable objetivo: `target`.
- Clases: `Privado` y `No_Privado`.
- La clase positiva para las métricas operativas es `No_Privado`.

El conjunto presenta un fuerte desbalance de clases: aproximadamente 99,59 % `Privado` y 0,41 % `No_Privado`.

## Cómo incorporar los datos localmente

1. Obtén el archivo de origen desde una fuente a la que tengas autorización de acceso.
2. Revisa sus condiciones de uso y evita publicar información personal o registros restringidos.
3. Guarda el archivo localmente y configura su ruta fuera del repositorio, o utiliza una carpeta ignorada por Git.
4. Ejecuta el notebook siguiendo el orden de sus secciones para reproducir la preparación y el entrenamiento.

No se incluye una ruta de archivo de origen porque debe confirmarse en el entorno donde se ejecuta el proyecto. Tampoco se debe inferir que el dataset puede redistribuirse públicamente.

## Privacidad y control de versiones

No subir datos personales, archivos fuente sin autorización, credenciales, ni archivos grandes generados localmente. El `.gitignore` del repositorio excluye ubicaciones habituales de datos privados; verifica las reglas antes de hacer un `git push`.
