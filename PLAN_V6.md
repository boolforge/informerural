# PLAN DE ACCIÓN V6.0: CREACIÓN DE `AGENT.md` v6.0

## 0. Propósito de este Documento

Este documento no es un resumen. Es un **plan de acción de nivel forense** que detalla, con la máxima granularidad, cada paso necesario para construir la versión 6.0 del `AGENT.md` y su ecosistema de soporte. Sirve como un contrato de trabajo entre el agente de IA y el operador humano (`boolforge`) para asegurar la alineación total antes de la ejecución. La aprobación de este documento implica la aprobación de cada punto detallado en él.

---

## 1. Parte 1: Análisis Multi-Arquetipo Extendido

Esta sección detalla el análisis de los arquetipos de usuario, que servirá como base para la nueva sección correspondiente en `AGENT.md` v6.0.

### 1.1. Análisis Profundo del Arquetipo Primario (El Anacoreta Resiliente)

El arquetipo primario es una amalgama compleja de necesidades que a menudo están en tensión. El análisis no puede ser lineal; debe ser interseccional.

*   **Intersección 1: (Hipersensibilidad + Patología Respiratoria) + (Necesidad de Autosuficiencia)**
    *   **Análisis:** La necesidad de "vivir de la tierra" implica una exposición constante al entorno local. Para una persona con hipersensibilidad a olores y alergias a polen/moho, esto significa que la calidad del aire y el ecosistema local no son solo métricas de "calidad de vida", sino factores de viabilidad existencial. Un lugar con alta humedad constante (riesgo de moho en la vivienda) o picos de polen de un taxón agresivo (abedul, ambrosía) es inviable, independientemente de otros factores positivos.
    *   **Implicación en el Plan:** El `Índice Respiratorio (IR)` debe tener un peso dominante y posiblemente un poder de veto no lineal. La recolección de datos sobre tipos de polen, humedad del suelo y calidad de la construcción local (ventilación, materiales) se vuelve crítica.

*   **Intersección 2: (TDAH + Dislexia) + (Entropía Burocrática)**
    *   **Análisis:** Un perfil con dificultades en la función ejecutiva (iniciar tareas, planificación) y en el procesamiento de texto complejo tiene una "Reserva de Energía para la Fricción Administrativa" extremadamente limitada. Un país con una burocracia opaca, analógica, con múltiples formularios complejos y en un idioma no accesible, representa una barrera infranqueable.
    *   **Implicación en el Plan:** Las métricas para "Hostilidad Cognitiva" y "Entropía Burocrática" deben ser priorizadas. Se deben buscar proxies concretos: ¿los trámites son 100% online? ¿Los formularios están disponibles en inglés? ¿Existen servicios de "ventanilla única"? Un país sin estas facilidades impone una carga existencial inaceptable.

*   **Intersección 3: (Valores Progresistas + Turismofobia) + (Código Social Implícito)**
    *   **Análisis:** El arquetipo busca un entorno no solo físicamente seguro, sino psicológicamente seguro. Un lugar con una tendencia política conservadora o un auge de la extrema derecha, aunque sea sutil, genera un estrés crónico. La "turismofobia" no es una simple preferencia; es una necesidad de autenticidad y de evitar la transitoriedad y la mercantilización del espacio vital.
    *   **Implicación en el Plan:** El `Índice de Progresismo y Seguridad Social (IPSS)` y el `Índice de Sostenibilidad y Bajo Turismo (ISBT)` son filtros cruciales. El análisis del "código social implícito" debe investigar activamente la tolerancia real a los "forasteros" (`outsiders`), más allá de la cortesía superficial.

### 1.2. Desarrollo de Arquetipos Secundarios

El sistema debe ser extensible. A continuación se detalla cómo se adaptaría la metodología para los tres arquetipos secundarios.

#### 1.2.1. El Tecnólogo Resiliente

*   **Perfil:** Prioriza conectividad digital de alta gama, acceso a servicios modernos, seguridad y networking profesional. Menos sensible a factores ambientales, más sensible a la infraestructura y la eficiencia.
*   **Adaptación de la Metodología:**
    *   **Re-ponderación de Índices:**
        *   `ICT (Conectividad y Trabajo)`: Pasa de 0.08 a **0.30** (máxima prioridad).
        *   `IAS (Acceso Sanitario)`: Se mantiene alto, enfocado en servicios modernos, **0.15**.
        *   `IPSS (Progresismo y Seguridad)`: Se mantiene alto, enfocado en seguridad física y estado de derecho, **0.20**.
        *   `IAR (Asequibilidad)`: Baja a **0.10**.
        *   `IR (Respiratorio)`: Baja a **0.05** (asume salud base).
        *   `ISBT (Sostenibilidad/Turismo)`: Baja a **0.05**.
        *   `RFC (Riesgo Climático)`: Se mantiene en **0.10**.
        *   `IAC (Aceptación Cultural)`: Baja a **0.05**.
    *   **Nuevos Datos Requeridos:** Latencia de red (ms) a los principales `IXP` europeos, fiabilidad de la red eléctrica (índice SAIDI/SAIFI), número de `coworking spaces` por 10k habitantes, tiempo de viaje a un aeropuerto internacional.
    *   **Cambios en Filtros Duros:** El filtro de `Tiempo a urgencias` podría flexibilizarse a 90 min si existe un helipuerto. Los filtros de PM2.5 y humedad se relajarían.

#### 1.2.2. La Familia Arraigada

*   **Perfil:** Prioriza seguridad comunitaria, calidad educativa (incl. necesidades especiales), sanidad pediátrica/geriátrica, espacios naturales y asequibilidad real de la vivienda.
*   **Adaptación de la Metodología:**
    *   **Re-ponderación de Índices:**
        *   `IAS (Acceso Sanitario)`: Pasa a **0.25**, con un sub-índice para pediatría/geriatría.
        *   `IPSS (Progresismo y Seguridad)`: Pasa a **0.25**, con énfasis en crimen local y seguridad comunitaria.
        *   `IAR (Asequibilidad)`: Se mantiene muy alto, **0.20**.
        *   `IAC (Aceptación Cultural)`: Sube a **0.10**, enfocado en cohesión comunitaria.
        *   `IR (Respiratorio)`: Se mantiene en un nivel base, **0.05**.
        *   `ICT (Conectividad)`: Baja a **0.05**.
        *   `RFC (Riesgo Climático)`: Se mantiene en **0.05**.
        *   `ISBT (Sostenibilidad/Turismo)`: Se mantiene en **0.05**.
    *   **Nuevos Datos Requeridos:** Calidad de las escuelas locales (ratio profesor/alumno, resultados estandarizados), disponibilidad de especialistas en educación especial, número de parques/zonas de juego, índice de criminalidad local (no solo regional), coste de actividades extraescolares.
    *   **Cambios en Filtros Duros:** El filtro de `Tiempo a urgencias` se mantiene estricto (60 min). Se podría añadir un filtro sobre la calidad mínima de las escuelas.

#### 1.2.3. El Productor Sostenible

*   **Perfil:** Prioriza calidad de suelo y agua, clima predecible, bajo coste de tierra, logística de distribución y redes de apoyo mutuo (cooperativas).
*   **Adaptación de la Metodología:**
    *   **Re-ponderación de Índices:**
        *   `IAR (Asequibilidad)`: Pasa a **0.30**, con énfasis en `€/ha suelo rústico`.
        *   `RFC (Riesgo Climático)`: Sube a **0.20**, con énfasis en sequía y predictibilidad climática.
        *   `ISBT (Sostenibilidad)`: Sube a **0.15**, enfocado en calidad de agua/suelo y normativas ambientales.
        *   `ICT (Conectividad)`: Se mantiene en **0.10** (para logística y ventas online).
        *   `IAC (Aceptación Cultural)`: Sube a **0.10**, enfocado en la existencia de cooperativas y mercados locales.
        *   `IR, IPSS, IAS`: Bajan a **0.05** cada uno.
    *   **Nuevos Datos Requeridos:** Análisis detallado de la calidad del suelo (pH, textura, materia orgánica), derechos de agua, regulaciones de zonificación agrícola (`zoning`), proximidad a mercados de agricultores, existencia de cooperativas agrícolas locales.
    *   **Cambios en Filtros Duros:** Se añadirían filtros sobre la calidad mínima del suelo y la disponibilidad de derechos de agua.

---

## 2. Parte 2: Especificación Técnica del Ecosistema de Herramientas

Esta sección detalla el diseño conceptual de una suite de herramientas de apoyo para automatizar, validar y facilitar el trabajo del agente. Se documentarán en `AGENT.md` y `base_de_conocimiento/scripts/README.md`.

### 2.1. Categoría: Adquisición de Datos

*   **`web_scraper.py`**
    *   **Propósito:** Script genérico y configurable para extraer datos de páginas web HTML.
    *   **Inputs:** `--url <URL>`, `--target-element <CSS_SELECTOR>`, `--output-format <json|csv>`
    *   **Lógica:** Usa `requests` y `BeautifulSoup4`. Navega a la URL, localiza los elementos mediante el selector CSS y extrae su contenido.
    *   **Output:** Imprime en `stdout` los datos en el formato especificado.
    *   **Manejo de Errores:** Captura errores de red (4xx, 5xx) y de parsing (elemento no encontrado).

*   **`api_client.py`**
    *   **Propósito:** Cliente genérico para interactuar con APIs REST.
    *   **Inputs:** `--endpoint <URL>`, `--params <'{"key":"value"}'>`, `--headers <'{"key":"value"}'>`, `--method <GET|POST>`
    *   **Lógica:** Usa `requests`. Construye y envía la petición. Parsea la respuesta JSON.
    *   **Output:** Imprime en `stdout` la respuesta JSON del servidor.
    *   **Manejo de Errores:** Maneja timeouts, errores de conexión y códigos de estado no-200.

*   **`pdf_extractor.py`**
    *   **Propósito:** Extraer tablas y texto de documentos PDF.
    *   **Inputs:** `--file <path_to_pdf>`, `--page <numero>`, `--table-area <x1,y1,x2,y2>` (opcional)
    *   **Lógica:** Usa librerías como `PyPDF2` o `pdfplumber`. Extrae texto plano o localiza tablas (si se proporciona un área) y las convierte a un formato estructurado.
    *   **Output:** CSV o JSON de la tabla extraída a `stdout`.

### 2.2. Categoría: Procesamiento y Validación de Datos

*   **`data_validator.py`**
    *   **Propósito:** Validar un archivo de datos (CSV) contra el esquema oficial de `23_esquema_dataset_final.md`.
    *   **Inputs:** `--file <path_to_csv>`
    *   **Lógica:** Carga el CSV. Compara los nombres de las columnas, el orden y los tipos de datos con el esquema maestro. Reporta cualquier discrepancia.
    *   **Output:** Un informe de validación en `stdout`. Devuelve código de salida 0 si es válido, 1 si hay errores.
    *   **Manejo de Errores:** Errores de lectura de archivo.

*   **`data_cleaner.py`**
    *   **Propósito:** Realizar operaciones de limpieza de datos, como la imputación de valores faltantes.
    *   **Inputs:** `--file <in_csv>`, `--output <out_csv>`, `--method <knn|mice|mean>`, `--columns <col1,col2>`
    *   **Lógica:** Usa `pandas` y `scikit-learn`. Aplica el método de imputación especificado a las columnas dadas.
    *   **Output:** Un nuevo archivo CSV con los datos limpios.

*   **`data_normalizer.py`**
    *   **Propósito:** Aplicar la normalización robusta (min-max p5-p95) a las columnas especificadas.
    *   **Inputs:** `--file <in_csv>`, `--output <out_csv>`, `--columns <col1,col2>`
    *   **Lógica:** Usa `pandas`. Calcula los percentiles 5 y 95 para cada columna, aplica clipping y luego la normalización min-max.
    *   **Output:** Un nuevo archivo CSV con las columnas normalizadas.

### 2.3. Categoría: Análisis

*   **`mca_engine.py`**
    *   **Propósito:** Calcular los índices finales y el ranking usando la metodología MCDA.
    *   **Inputs:** `--data <path_to_csv>`, `--config <path_to_config.yaml>`
    *   **Lógica:** Carga los datos y los pesos/parámetros del `config.yaml`. Calcula los 8 índices compuestos. Aplica TOPSIS para generar un ranking final.
    *   **Output:** El CSV original enriquecido con las columnas de índices y ranking.

### 2.4. Categoría: Reporte y Utilidad

*   **`report_generator.py`**
    *   **Propósito:** Generar un borrador de informe en Markdown para una localidad dada.
    *   **Inputs:** `--data <path_to_csv>`, `--locality-id <ID>`
    *   **Lógica:** Usa la plantilla de `ejemplo_informe_final.md`. Carga los datos para la localidad especificada y rellena la plantilla con los valores cuantitativos y cualitativos.
    *   **Output:** Un nuevo archivo `.md` para esa localidad.

*   **`progress_updater.py`**
    *   **Propósito:** Actualizar automáticamente el archivo de progreso.
    *   **Inputs:** `--task-id <ID_de_tarea>`, `--status <complete|pending>`
    *   **Lógica:** Parsea `25_plan_de_trabajo_y_progreso.md`, busca la línea de la tarea y actualiza su checkbox (`[ ]` a `[x]`).
    *   **Output:** El archivo de plan de trabajo modificado.

*   **`issue_reporter.py`**
    *   **Propósito:** Formalizar la escalada de errores.
    *   **Inputs:** `--title "<título>"`, `--body "<descripción>"`, `--labels <bug,critical>`
    *   **Lógica:** Crea un archivo de informe de incidencia en `logs/incidents/`. Si existiera una API de un gestor de issues (como GitHub Issues), interactuaría con ella.
    *   **Output:** Mensaje de confirmación.

---

## 3. Parte 3: Blueprint de `AGENT.md` v6.0

Esta sección es el esquema detallado del contenido del `AGENT.md` final.

*   **Sección 1: Directiva Maestra:** Incluirá el rol explícito ("ASUMA EL ROL...") y la misión de deconstrucción forense.
*   **Sección 2: Análisis Multi-Arquetipo:** Incluirá el análisis interseccional del arquetipo primario y el análisis de adaptación para los tres arquetipos secundarios.
*   **Sección 3: Protocolo Operativo Cognitivo (POC):** Incluirá el bucle de 5 pasos, la excepción para micro-tareas y una nueva sub-sección sobre "Estrategias de Caching" para evitar la re-lectura de archivos críticos.
*   **Sección 4: Protocolo de Registro de Actividad (PRA):** Incluirá el propósito de la bitácora y las dos plantillas (completa y resumida).
*   **Sección 5: Protocolo de Manejo de Fallos (PMF):** Incluirá la lógica de reintento, reversión y escalado, y definirá los tipos de errores (`NETWORK_ERROR`, `LOGIC_ERROR`).
*   **Sección 6: Protocolo Operacional de Entorno (POE):** Incluirá la regla de la bóveda enmendada y el flujo de Git autorizado (sin el token hardcodeado).
*   **Sección 7: Protocolo de Investigación:** Referenciará los documentos de plan de trabajo y metodología.
*   **Sección 8: Suite de Herramientas y Scripts:** Un manual didáctico para el ecosistema de herramientas diseñado en la Parte 2.
*   **Sección 9: Guía Forense de la Base de Conocimiento:** Una descripción detallada de CADA archivo del repositorio.
*   **Sección 10: Operacionalización de Conceptos:** Ejemplos de cómo convertir conceptos abstractos en métricas.

---

## 4. Parte 4: Hoja de Ruta de Implementación

Este es el checklist de acciones que se tomarán una vez este plan sea aprobado.

1.  **[ ] Crear `base_de_conocimiento/dependencies.md`:** Documentar todas las dependencias técnicas.
2.  **[ ] Crear `base_de_conocimiento/scripts/README.md`:** Crear el archivo que albergará el manual de herramientas.
3.  **[ ] Crear `base_de_conocimiento/ejemplo_informe_final.md`:** Crear el archivo de ejemplo para el informe.
4.  **[ ] Crear `logs/incidents/`:** Crear el directorio para los informes de incidencias.
5.  **[ ] Actualizar `AGENT.md` a v6.0:** Reemplazar el contenido del `AGENT.md` actual con el nuevo contenido detallado en el Blueprint.
6.  **[ ] Verificar todos los cambios:** Usar `ls -R` y `read_file` en todos los archivos nuevos y modificados para asegurar la integridad.
7.  **[ ] Enviar para Revisión Final:** Usar la herramienta `submit` para proponer todos los cambios.
