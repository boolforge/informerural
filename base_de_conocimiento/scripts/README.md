# Manual de la Suite de Herramientas y Scripts

Este documento sirve como manual de usuario didáctico para el ecosistema de scripts de apoyo del proyecto `informerural`.

## Filosofía de Diseño

Las herramientas están diseñadas para ser:
*   **Modulares y de Propósito Único:** Cada script realiza una tarea bien definida.
*   **Configurables por Línea de Comandos:** Aceptan argumentos para flexibilidad.
*   **Basadas en `stdout`:** Imprimen resultados en la salida estándar para permitir el encadenamiento (`piping`) y la composición.
*   **Robustas:** Incluyen manejo de errores básicos.

## 1. Categoría: Adquisición de Datos

Scripts diseñados para obtener datos de fuentes externas.

### `web_scraper.py`
*   **Propósito:** Extraer datos de páginas web HTML.
*   **Uso:** `python web_scraper.py --url <URL> --target-element <CSS_SELECTOR>`
*   **Ejemplo:** `python web_scraper.py --url "https://.../cost-of-living" --target-element ".data-table"`

### `api_client.py`
*   **Propósito:** Cliente genérico para APIs REST.
*   **Uso:** `python api_client.py --endpoint <URL> --params '{"key":"value"}'`

### `pdf_extractor.py`
*   **Propósito:** Extraer tablas y texto de documentos PDF.
*   **Uso:** `python pdf_extractor.py --file <path_to_pdf> --page <num>`

## 2. Categoría: Procesamiento y Validación

Scripts para limpiar, validar y transformar datos.

### `data_validator.py`
*   **Propósito:** Validar un CSV contra el esquema oficial.
*   **Uso:** `python data_validator.py --file <path_to_csv>`
*   **Lógica:** Compara columnas y tipos de datos con `base_de_conocimiento/metodologia/23_esquema_dataset_final.md`. Devuelve un código de salida 0 si es válido.

### `data_cleaner.py`
*   **Propósito:** Imputar valores faltantes.
*   **Uso:** `python data_cleaner.py --file <in.csv> --output <out.csv> --method <mean>`

### `data_normalizer.py`
*   **Propósito:** Aplicar la normalización robusta p5-p95.
*   **Uso:** `python data_normalizer.py --file <in.csv> --output <out.csv> --columns "col1,col2"`

## 3. Categoría: Análisis

Scripts que realizan los cálculos analíticos del proyecto.

### `mca_engine.py`
*   **Propósito:** Calcular los índices y el ranking MCDA.
*   **Uso:** `python mca_engine.py --data <data.csv> --config <config.yaml>`
*   **Lógica:** Carga los datos y los pesos del `config.yaml`, calcula los 8 índices y aplica TOPSIS.

## 4. Categoría: Reporte y Utilidad

Scripts para generar artefactos y gestionar el flujo de trabajo.

### `report_generator.py`
*   **Propósito:** Generar un borrador de informe para una localidad.
*   **Uso:** `python report_generator.py --data <data.csv> --locality-id <ID>`
*   **Lógica:** Usa la plantilla de `ejemplo_informe_final.md`.

### `progress_updater.py`
*   **Propósito:** Actualizar el archivo de plan de trabajo.
*   **Uso:** `python progress_updater.py --task-id <ID_de_tarea> --status complete`

### `issue_reporter.py`
*   **Propósito:** Formalizar la escalada de errores.
*   **Uso:** `python issue_reporter.py --title "Error Crítico" --body "Descripción..."`
*   **Lógica:** Crea un archivo de incidencia en `logs/incidents/`.
