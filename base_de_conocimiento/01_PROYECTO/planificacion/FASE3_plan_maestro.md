# FASE 3: Plan Maestro de Ejecución - Guardián del Conocimiento V2

**Estado:** Borrador. No ejecutar hasta recibir aprobación explícita.

---

## Introducción
Este documento detalla el plan de ejecución para la FASE 3 del proyecto, siguiendo el protocolo "Guardián del Conocimiento V2". El plan se divide en tres grandes ejes que se ejecutarán de forma entrelazada: desarrollo de un ecosistema de herramientas robustas, creación de una arquitectura geográfica de conocimiento y consolidación del contenido existente.

---

## Eje I: Plan de Desarrollo del Ecosistema de Herramientas
El desarrollo de cada herramienta seguirá rigurosamente el **Ciclo de Desarrollo de Herramientas (CDH) Paranoico** de 5 fases para garantizar su máxima calidad y fiabilidad.

### 1. Herramienta: "Cartographer"
*   **Misión:** Automatizar la creación de la estructura de directorios geográficos y la generación de sus `_metadata.json`.
*   **Plan de Desarrollo (CDH):**
    *   **Fase 1 (Manual/Ground Truth):** Realizaré manualmente la investigación para un país (ej. España), documentando su jerarquía administrativa completa y creando la estructura de directorios y los archivos `_metadata.json` a mano. Este resultado perfecto será mi "Ground Truth".
    *   **Fase 2 (Prototipo):** Investigaré APIs geográficas (e.g., GeoNames, OpenStreetMap Nominatim) y librerías de Python (`os`, `json`) para desarrollar un script MVP que pueda replicar la estructura de España.
    *   **Fase 3 (Refinamiento):** Compararé la salida del script con mi "Ground Truth" y lo refinaré iterativamente hasta que el resultado sea 100% idéntico.
    *   **Fase 4 (Estrés):** Probaré el script con países con estructuras administrativas complejas (ej. Reino Unido, Japón, Alemania) y casos de borde (datos faltantes, caracteres especiales).
    *   **Fase 5 (Integración):** Una vez superadas las pruebas, la herramienta estará lista para su uso en el Eje II.

### 2. Herramienta: "Janitor"
*   **Misión:** Limpiar, validar, estandarizar y transformar datos crudos.
*   **Plan de Desarrollo (CDH):**
    *   **Fase 1 (Manual/Ground Truth):** Tomaré un archivo de datos crudos (ej. un CSV de calidad del aire) y lo limpiaré manualmente, documentando cada paso (ej. eliminar duplicados, corregir formatos, imputar valores).
    *   **Fase 2 (Prototipo):** Desarrollaré un script con `pandas` o `polars` que replique estas operaciones de forma programática.
    *   **Fases 3-5:** Seguiré el ciclo de refinamiento, pruebas de estrés (con datos malformados, grandes volúmenes) e integración.

### 3. Herramientas: "Scout", "Weaver", y "Auditor"
*   **Misión:** (Scout) Recopilar datos; (Weaver) Hiper-indexar el contenido; (Auditor) Verificar la integridad del repositorio.
*   **Plan de Desarrollo (CDH):** Estas herramientas se desarrollarán de forma modular e incremental a medida que surja la necesidad durante la consolidación. Por ejemplo, se creará un "Scout" específico para una fuente de datos, se probará rigurosamente y luego se usará. El "Weaver" comenzará con una función simple de enlace y evolucionará. El "Auditor" se construirá al final para validar la estructura final.

---

## Eje II: Plan de Ejecución del Andamiaje de Datos (Data Scaffolding)
Este plan se ejecutará utilizando la herramienta "Cartographer" una vez que esté validada.

1.  **País Piloto (España):** Utilizaré España como el primer caso de uso para el andamiaje de datos, ya que fue el "Ground Truth" para el desarrollo de Cartographer.
2.  **Expansión a Países Clave:** Procederé con los siguientes países en orden de prioridad, según su relevancia en el análisis: Reino Unido, Japón, Alemania, Francia, y otros países de alto desarrollo que se identifiquen.
3.  **Verificación Continua:** Después de cada ejecución de Cartographer para un país, realizaré una verificación manual de la estructura creada para asegurar la calidad y corregir cualquier desviación.

---

## Eje III: Plan de Consolidación de Candidatos
Este plan se ejecutará en paralelo con los otros ejes, utilizando las nuevas herramientas y aplicando sus decisiones.

1.  **Consolidación Candidato #5 (Prompts Históricos):**
    *   **Acción:** Leeré el contenido de `informes/08_proximos_pasos_prompt_1.md` y `informes/09_proximos_pasos_prompt_2.md`. Lo anexaré al final de `logs/bitacora_agente.md` bajo una nueva sección `## Apéndice: Prompts Históricos`. Finalmente, marcaré los archivos originales como históricos (propondré su eliminación o archivo en FASE 3, según su preferencia final).
    *   **Herramientas:** `read_file`, `replace_with_git_merge_diff`.

2.  **Consolidación Candidato #3 (Metodología):**
    *   **Acción:** Usando `metodologia/00_directiva_filosofica.md` como base, fusionaré el contenido de `01_rol_y_directiva.md` y `02_pasaporte_de_necesidades.md`. Deduplicaré y enriqueceré el contenido para crear una directiva robusta. Renombraré el archivo final a `metodologia/00_project_charter_consolidado.md`.
    *   **Herramientas:** `read_file`, `create_file_with_block`, `delete_file` (para los archivos originales fusionados, marcándolos como históricos).

3.  **Consolidación Candidato #4 (Clasificación Rural):**
    *   **Acción:** Crearé el archivo maestro `metodologia/metodologia_clasificacion_rural.md` con la teoría general. A medida que se realice el andamiaje de cada país (Eje II), crearé los informes de clasificación aplicada en su correspondiente directorio geográfico.
    *   **Herramientas:** `create_file_with_block`, "Cartographer".

4.  **Consolidación Candidato #2 (Polen) y #1 (País Fragmentada):**
    *   **Acción:** Estas dos tareas están intrínsecamente ligadas y son el corazón de la refactorización. A medida que la estructura de directorios de cada país se cree (Eje II), desmantelaré `02_macro_contextual.md` y los archivos de `investigacion/`. Moveré y estructuraré la información (incluyendo el análisis de polen) en los nuevos directorios de país.
    *   **Herramientas:** "Janitor" para limpiar y estructurar los fragmentos de texto; "Scout" para verificar y enriquecer datos; "Weaver" para enlazar conceptos.

5.  **Consolidación Candidato #6 (Índice):**
    *   **Acción:** Esta será la última tarea. Una vez que toda la estructura esté en su lugar, ejecutaré la estrategia híbrida:
        1.  Crearé el `indice.md` manualmente.
        2.  Desarrollaré el script `scripts/generar_indice.py` (siguiendo el CDH Paranoico).
        3.  Refinaré el script hasta que su salida coincida con la versión manual.
    *   **Herramientas:** `create_file_with_block`, herramientas de desarrollo de Python.
