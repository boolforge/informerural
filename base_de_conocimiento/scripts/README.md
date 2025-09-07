# Manual de la Suite de Herramientas y Scripts

Este documento sirve como manual de usuario didáctico para el ecosistema de scripts de apoyo del proyecto `informerural`.

## Filosofía de Diseño

Las herramientas están diseñadas para ser:
*   **Modulares y de Propósito Único:** Cada script realiza una tarea bien definida.
*   **Configurables por Línea de Comandos:** Aceptan argumentos para flexibilidad.
*   **Robustas:** Incluyen manejo de errores y están diseñadas para funcionar de manera fiable en el entorno del agente.

## 0. Categoría: Gestión de Archivos (Portable)

Scripts que reemplazan las herramientas nativas del agente para asegurar la portabilidad.

### `file_manager.py` - [IMPLEMENTADO]
*   **Propósito:** Encapsular todas las operaciones básicas del sistema de archivos (CRUD) para que el flujo de trabajo sea replicable por cualquier agente.
*   **Uso:** `python file_manager.py [comando] [argumentos]`
*   **Comandos:**
    *   `create <path> [--content-file <path>]`: Crea un nuevo archivo. Si se pasa `--content-file`, usa el contenido de ese archivo.
    *   `read <path>`: Lee y muestra el contenido de un archivo a `stdout`.
    *   `overwrite <path> --content-file <path>`: Sobrescribe un archivo con el contenido del archivo especificado.
    *   `delete <path>`: Borra un archivo.
*   **Ejemplo (Overwrite):** `python file_manager.py overwrite "archivo_a_sobrescribir.txt" --content-file "nuevo_contenido.txt"`

## 1. Categoría: Adquisición de Datos (Implementados)\n\n### `analyze_multiple_sites_1_1.py` - [NO FUNCIONAL]\n*   **Propósito (Inferido):** Analizar datos de calidad del aire de múltiples sitios.\n*   **Estado:** CORRUPTO. Falla la verificación de sintaxis (`SyntaxError: unexpected character after line continuation character`). No debe ser ejecutado.\n*   **Acción Recomendada:** Eliminar o reparar.\n\n### `download_copernicus_air_quality_4.py` - [NO FUNCIONAL]\n*   **Propósito (Inferido):** Descargar datos de calidad del aire del servicio Copernicus.\n*   **Estado:** CORRUPTO. Falla la verificación de sintaxis (`SyntaxError: unexpected character after line continuation character`). No debe ser ejecutado.\n*   **Acción Recomendada:** Eliminar o reparar.\n\n### `download_eea_air_quality_1.py` - [NO FUNCIONAL]\n*   **Propósito (Inferido):** Descargar datos de calidad del aire de la EEA.\n*   **Estado:** CORRUPTO. Falla la verificación de sintaxis (`SyntaxError: unexpected character after line continuation character`). No debe ser ejecutado.\n*   **Acción Recomendada:** Eliminar o reparar.\n\n### `download_eurostat_social_protection.py` - [FUNCIONAL]\n*   **Propósito (Inferido):** Descargar datos de protección social de Eurostat.\n*   **Estado:** FUNCIONAL. Pasa la verificación de sintaxis.\n*   **Acción Recomendada:** Utilizar según sea necesario.\n\n### `download_gadm_data.py` - [FUNCIONAL]\n*   **Propósito (Inferido):** Descargar datos geoespaciales de GADM.\n*   **Estado:** FUNCIONAL. Pasa la verificación de sintaxis.\n*   **Acción Recomendada:** Utilizar según sea necesario.\n\n## 1. Categoría: Adquisición de Datos (Conceptual)

Scripts diseñados para obtener datos de fuentes externas.

### `web_scraper.py`
*   **Propósito:** Extraer datos de páginas web HTML.
*   **Uso:** `python web_scraper.py --url <URL> --target-element <CSS_SELECTOR>`

### `api_client.py`
*   **Propósito:** Cliente genérico para APIs REST.
*   **Uso:** `python api_client.py --endpoint <URL> --params '{"key":"value"}'`

### `pdf_extractor.py`
*   **Propósito:** Extraer tablas y texto de documentos PDF.
*   **Uso:** `python pdf_extractor.py --file <path_to_pdf> --page <num>`

## 2. Categoría: Procesamiento y Validación (Conceptual)

Scripts para limpiar, validar y transformar datos.

### `data_validator.py`
*   **Propósito:** Validar un CSV contra el esquema oficial.
*   **Uso:** `python data_validator.py --file <path_to_csv>`

### `data_cleaner.py`
*   **Propósito:** Imputar valores faltantes.
*   **Uso:** `python data_cleaner.py --file <in.csv> --output <out.csv> --method <mean>`

### `data_normalizer.py`
*   **Propósito:** Aplicar la normalización robusta p5-p95.
*   **Uso:** `python data_normalizer.py --file <in.csv> --output <out.csv> --columns "col1,col2"`

## 3. Categoría: Análisis (Conceptual)

Scripts que realizan los cálculos analíticos del proyecto.

### `mca_engine.py`
*   **Propósito:** Calcular los índices y el ranking MCDA.
*   **Uso:** `python mca_engine.py --data <data.csv> --config <config.yaml>`

## 4. Categoría: Reporte y Utilidad (Conceptual)

Scripts para generar artefactos y gestionar el flujo de trabajo.

### `report_generator.py`
*   **Propósito:** Generar un borrador de informe en Markdown para una localidad dada.
*   **Uso:** `python report_generator.py --data <data.csv> --locality-id <ID>`

### `progress_updater.py`
*   **Propósito:** Actualizar el archivo de plan de trabajo.
*   **Uso:** `python progress_updater.py --task-id <ID_de_tarea> --status complete`

### `issue_reporter.py`
*   **Propósito:** Formalizar la escalada de errores.
*   **Uso:** `python issue_reporter.py --title "Error Crítico" --body "Descripción..."`

### `update_checkpoint.py`
*   **Propósito:** Crear y actualizar un punto de control de estado para el agente.
*   **Uso:** `python update_checkpoint.py --last-action "<descripción>" --next-step "<descripción>" --status "<ÉXITO|FRACASO>"`
