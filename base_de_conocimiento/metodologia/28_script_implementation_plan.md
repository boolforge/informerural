# Plan de Implementación de Scripts (v1 - Jules)

**Propietario:** Agente Jules
**Fecha de Creación:** 2025-09-06
**Propósito:** Priorizar y gestionar la implementación de la suite de herramientas conceptuales documentadas en `scripts/README.md`.

---

## Filosofía
La implementación seguirá un orden lógico, priorizando las herramientas que ofrezcan el mayor impacto en la robustez y eficiencia del flujo de trabajo del agente. Cada implementación seguirá el ciclo de `Diseñar -> Implementar -> Documentar -> Probar`.

---

## Roadmap de Implementación

### Prioridad 1: Herramientas de Flujo de Trabajo y Estado
*Estas herramientas son críticas para la fiabilidad y la adherencia al protocolo del agente.*

*   **[ ] `update_checkpoint.py`**
    *   **Estado:** Conceptual.
    *   **Tarea:** Implementar el script para leer y escribir en `checkpoint.json`, asegurando la persistencia del estado entre acciones.
*   **[ ] `progress_updater.py`**
    *   **Estado:** Conceptual.
    *   **Tarea:** Implementar el script para parsear y modificar el archivo de plan de trabajo maestro, permitiendo la actualización automática del progreso.
*   **[ ] `issue_reporter.py`**
    *   **Estado:** Conceptual.
    *   **Tarea:** Implementar la creación de archivos de incidencia en `logs/incidents/`. La integración con una API externa (ej. GitHub) se considera un `stretch goal`.

### Prioridad 2: Herramientas de Procesamiento y Validación de Datos
*Estas herramientas son esenciales para asegurar la calidad y consistencia de los datos antes del análisis.*

*   **[ ] `data_validator.py`**
    *   **Estado:** Conceptual.
    *   **Tarea:** Implementar la lógica de validación contra el esquema maestro (`23_esquema_dataset_final.md`). Debe ser capaz de verificar columnas, tipos de datos y rangos.
*   **[ ] `data_normalizer.py`**
    *   **Estado:** Conceptual.
    *   **Tarea:** Implementar la función de normalización robusta (p5-p95).
*   **[ ] `data_cleaner.py`**
    *   **Estado:** Conceptual.
    *   **Tarea:** Implementar al menos un método de imputación simple (ej. `mean` o `median`). Métodos más complejos como `knn` o `mice` son `stretch goals`.

### Prioridad 3: Herramientas de Adquisición de Datos
*Estas herramientas mejorarán la capacidad del agente para recopilar nuevos datos de forma autónoma.*

*   **[ ] `api_client.py`**
    *   **Estado:** Conceptual.
    *   **Tarea:** Implementar un cliente de API REST genérico y robusto.
*   **[ ] `web_scraper.py`**
    *   **Estado:** Conceptual.
    *   **Tarea:** Implementar el scraper genérico basado en selectores CSS.
*   **[ ] `pdf_extractor.py`**
    *   **Estado:** Conceptual.
    *   **Tarea:** Implementar la extracción de texto. La extracción de tablas se considera un `stretch goal`.

### Prioridad 4: Herramientas de Análisis y Reporte
*Estas herramientas son el paso final y automatizan la generación de los entregables.*

*   **[ ] `mca_engine.py`**
    *   **Estado:** Conceptual.
    *   **Tarea:** Implementar el motor de cálculo de índices y ranking TOPSIS.
*   **[ ] `report_generator.py`**
    *   **Estado:** Conceptual.
    *   **Tarea:** Implementar la generación de informes en Markdown a partir de la plantilla y los datos.
