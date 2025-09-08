# Plan Maestro de Consolidación y Refactorización

**Estado:** Activo.
**Prioridad:** Máxima. Ejecutar antes de cualquier tarea de generación de datos.

## 1. Introducción
Este documento detalla el plan de ejecución para la Fase 1 del proyecto, enfocada en la consolidación, deduplicación, refactorización e hiper-indexación del contenido existente en la `base_de_conocimiento`. Este plan precede a la fase de andamiaje de datos geográficos.

## 2. Tareas de Consolidación

### Tarea 2.1: Consolidar Documentos de Metodología
*   **Estado:** Pendiente.
*   **Archivos de Origen:**
    *   `base_de_conocimiento/metodologia/00_directiva_filosofica.md`
    *   `base_de_conocimiento/metodologia/01_rol_y_directiva.md`
    *   `base_de_conocimiento/metodologia/02_pasaporte_de_necesidades.md`
    *   ... (y otros archivos relevantes en `/metodologia/`)
*   **Acción:**
    1.  Leer todos los archivos de metodología para entender su contenido y redundancias.
    2.  Fusionar todos los conceptos en un único documento maestro y coherente.
    3.  El nuevo documento se llamará `base_de_conocimiento/metodologia/00_acta_de_proyecto_consolidada.md`, siguiendo la directiva de nomenclatura en español.
    4.  Eliminar los archivos de origen una vez que su contenido haya sido migrado y verificado.
*   **Verificación:** El nuevo archivo debe existir y los archivos originales deben ser eliminados.

### Tarea 2.2: Archivar Prompts Históricos
*   **Estado:** Pendiente.
*   **Archivos de Origen:**
    *   `base_de_conocimiento/informes/08_proximos_pasos_prompt_1.md`
    *   `base_de_conocimiento/informes/09_proximos_pasos_prompt_2.md`
*   **Acción:**
    1.  Anexar el contenido completo de los archivos de prompts al final de `logs/bitacora_agente.md`.
    2.  La nueva sección se llamará `## Apéndice: Prompts Históricos`.
    3.  Eliminar los archivos de origen.
*   **Verificación:** La bitácora debe contener el apéndice y los archivos originales deben ser eliminados.

### Tarea 2.3: Refactorizar y Centralizar la Clasificación Rural
*   **Estado:** Pendiente.
*   **Archivos de Origen:**
    *   `base_de_conocimiento/investigacion/temas/07_clasificacion_rural_urbana_uk.md`
    *   `base_de_conocimiento/metodologia/21_clasificacion_rural_urbana_metodologia.md`
*   **Acción:**
    1.  Crear un único archivo maestro en `base_de_conocimiento/metodologia/metodologia_clasificacion_rural.md`.
    2.  Este archivo contendrá la teoría general (ej. DEGURBA) y luego secciones específicas para la aplicación en cada país (ej. la metodología del Reino Unido).
    3.  Eliminar los archivos de origen.
*   **Verificación:** El nuevo archivo debe existir y los archivos originales deben ser eliminados.

## 3. Estrategia de Hiper-Indexación y Deduplicación
*   **Estado:** Pendiente.
*   **Objetivo:** Transformar la base de conocimiento en un grafo de conocimiento navegable, eliminando la información repetida.
*   **Acciones:**
    1.  **Análisis de Redundancia:** Durante la consolidación, identificar activamente información duplicada (ej. `18_inventario_de_fuentes.md` vs `09_fuentes_de_datos.md`). El contenido debe ser fusionado en un único archivo canónico y el otro eliminado.
    2.  **Creación de un Glosario Central:** Crear un archivo `base_de_conocimiento/glosario.md` que defina términos clave (ej. "Carga Alostática", "Fricción Existencial", "DEGURBA").
    3.  **Implementación de Hipervínculos:** A medida que se procesan los archivos, se deben insertar activamente hipervínculos (usando sintaxis de Markdown `[texto](./ruta/al/archivo.md)`) que conecten los conceptos. Por ejemplo, cada vez que se mencione "Carga Alostática" en un documento, debe enlazar al `glosario.md`.
    4.  **Desarrollo de la Herramienta `Weaver`:** En una fase posterior (Fase 2 del plan general), se desarrollará un script para automatizar y auditar estos enlaces. Por ahora, el trabajo será manual y metódico.

## 4. Plan de Entrega
*   Al finalizar todas las tareas de este plan, se realizará un `commit` para guardar el estado consolidado de la base de conocimiento.
*   Solo entonces se procederá con la Fase 2: Andamiaje de Datos.
