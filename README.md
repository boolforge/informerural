# Repositorio de Investigación de Ecosistemas Rurales

Este repositorio contiene una base de conocimiento exhaustiva y una suite de herramientas para analizar y comparar ecosistemas rurales en base a un conjunto de indicadores cuantitativos y cualitativos. El objetivo es identificar localidades óptimas para un arquetipo de usuario específico.

La estructura ha sido reorganizada y optimizada para su uso por un agente de IA.

## Estructura del Repositorio

Toda la información y lógica del proyecto se encuentra dentro del directorio `base_de_conocimiento/`. La estructura es la siguiente:

### `/base_de_conocimiento`

*   **`/00_PROTOCOLO/`**: Contiene los documentos que definen el "cómo" del proyecto.
    *   `AGENT.md`: La directiva maestra que gobierna el comportamiento del agente de IA.
    *   `METODOLOGIA_INVESTIGACION.md`: El documento consolidado que detalla la metodología completa del análisis, incluyendo los índices, las fuentes de datos y los criterios de evaluación.
    *   `dependencies.md`: Las dependencias técnicas del proyecto.

*   **`/01_PROYECTO/`**: Archivos relacionados con la gestión y el histórico del proyecto.
    *   `ARCHIVADO_metodologia/` y `ARCHIVADO_informes/`: Versiones antiguas y fragmentadas de los documentos de metodología e informes, conservadas para el histórico.
    *   `configuracion/`: Archivos de configuración, como claves de API.
    *   Otros archivos de planificación y estado (`PLAN_V6.md`, `checkpoint.json`).

*   **`/02_CONOCIMIENTO/`**: El núcleo de la base de conocimiento, con la investigación y los datos cualitativos.
    *   `investigacion/`: Contiene la investigación cualitativa consolidada por país (`INVESTIGACION_CUALITATIVA_PAISES.md`) y otros análisis temáticos específicos.
    *   `audits/`, `historico/`: Auditorías e histórico del comportamiento de los agentes.
    *   `paises/`: **(Directorio problemático)** Contiene miles de archivos JSON con datos geográficos. Este directorio no pudo ser movido o eliminado debido a limitaciones del entorno. Sus datos han sido consolidados en `03_DATOS/gazetteer.csv`.

*   **`/03_DATOS/`**: Todos los datos cuantitativos del proyecto.
    *   `gazetteer.csv`: El archivo CSV consolidado con todos los datos geográficos de las localidades.
    *   `datos/crudos/`: Los datasets originales en formato CSV y JSON.
    *   `imagenes/`: Visualizaciones y gráficos generados.

*   **`/04_SCRIPTS/`**: Todos los scripts de Python utilizados en el proyecto.
    *   `consolidate_gazetteer.py`: El script utilizado para consolidar los datos del directorio `paises`.
    *   `scripts/`: El resto de los scripts para descarga y análisis de datos.

*   **`/05_REGISTROS/`**: Los registros de actividad del agente.
    *   `logs/bitacora_agente.md`: El registro detallado de todas las acciones realizadas por el agente.

## Tareas Pendientes
Para un detalle de las tareas que no se pudieron completar debido a limitaciones del entorno, por favor consulte el archivo `TAREAS_PENDIENTES.md` en la raíz de este repositorio.
