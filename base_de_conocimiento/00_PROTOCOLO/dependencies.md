# Dependencias Técnicas del Proyecto

Este documento detalla las dependencias técnicas necesarias para ejecutar los scripts y análisis de este repositorio.

## 1. Entorno de Ejecución

*   **Sistema Operativo:** Se asume un entorno basado en Linux (compatible con `bash`).
*   **Intérprete de Python:** Se requiere Python 3.8 o superior.

## 2. Librerías de Python

Los scripts de este proyecto dependen de varias librerías de Python. Deben ser instaladas a través de `pip`. Se recomienda el uso de un entorno virtual (`venv`) para gestionar las dependencias.

Un archivo `requirements.txt` debería ser creado y mantenido en la raíz del repositorio con el siguiente contenido mínimo:

```
# Fichero: requirements.txt
pandas
numpy
requests
beautifulsoup4
PyPDF2
pdfplumber
scikit-learn
pygadm
PyYAML
```

*   **pandas, numpy:** Para la manipulación y análisis de datos.
*   **requests, beautifulsoup4:** Para adquisición de datos web (`web_scraper.py`).
*   **PyPDF2, pdfplumber:** Para la extracción de datos de PDFs (`pdf_extractor.py`).
*   **scikit-learn:** Para la imputación de datos (`data_cleaner.py`).
*   **pygadm:** Para la descarga de datos geográficos.
*   **PyYAML:** Para leer el archivo de configuración `config.yaml`.

## 3. Herramientas del Entorno del Agente

El agente de IA depende de un conjunto de herramientas proporcionadas por su entorno de ejecución. Estas herramientas no requieren instalación manual, pero su presencia y funcionamiento son críticos. (Ej: `read_file`, `create_file_with_block`, `submit`, etc.).

## 4. Variables de Entorno

*   **`GITHUB_TOKEN`:** (Recomendación de seguridad) Variable que debería contener el token de acceso personal de GitHub para la autenticación. El `AGENT.md` instruye cómo usar esta variable si está disponible.
*   **`COPERNICUS_API_KEY`:** Variable que podría contener una clave de API para el Copernicus Data Store.
*   **`OTHER_API_KEYS`:** Otras claves para APIs de datos geoespaciales o socioeconómicos.
