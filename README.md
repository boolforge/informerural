# Repositorio de Investigación de Ecosistemas Rurales

Este repositorio contiene una base de conocimiento exhaustiva y una suite de herramientas para analizar y comparar ecosistemas rurales en base a un conjunto de indicadores cuantitativos y cualitativos. El objetivo es identificar localidades óptimas para un arquetipo de usuario específico.

La estructura ha sido reorganizada y optimizada para su uso por un agente de IA.

## Estructura del Repositorio

Toda la información y lógica del proyecto se encuentra dentro del directorio [`base_de_conocimiento/`](./base_de_conocimiento/). La estructura es la siguiente:

### [`/base_de_conocimiento`](./base_de_conocimiento/)

*   **[`/00_PROTOCOLO/`](./base_de_conocimiento/00_PROTOCOLO/)**: Contiene los documentos que definen el "cómo" del proyecto.
    *   [`AGENT.md`](./base_de_conocimiento/00_PROTOCOLO/AGENT.md): La directiva maestra que gobierna el comportamiento del agente de IA.
    *   [`METODOLOGIA_INVESTIGACION.md`](./base_de_conocimiento/00_PROTOCOLO/METODOLOGIA_INVESTIGACION.md): El documento consolidado que detalla la metodología completa del análisis.
    *   [`dependencies.md`](./base_de_conocimiento/00_PROTOCOLO/dependencies.md): Las dependencias técnicas del proyecto.

*   **[`/01_PROYECTO/`](./base_de_conocimiento/01_PROYECTO/)**: Archivos relacionados con la gestión y el histórico del proyecto.
    *   `ARCHIVADO_metodologia/` y `ARCHIVADO_informes/`: Versiones antiguas de documentos, conservadas para el histórico.
    *   [`configuracion/`](./base_de_conocimiento/01_PROYECTO/configuracion/): Archivos de configuración, como claves de API.
    *   Otros archivos de planificación y estado ([`PLAN_V6.md`](./base_de_conocimiento/01_PROYECTO/PLAN_V6.md), [`checkpoint.json`](./base_de_conocimiento/01_PROYECTO/checkpoint.json)).

*   **[`/02_CONOCIMIENTO/`](./base_de_conocimiento/02_CONOCIMIENTO/)**: El núcleo de la base de conocimiento.
    *   [`investigacion/`](./base_de_conocimiento/02_CONOCIMIENTO/investigacion/): Contiene la investigación cualitativa consolidada por país y otros análisis temáticos.
    *   `audits/`, `historico/`: Auditorías e histórico del comportamiento de los agentes.
    *   `paises/`: **(Directorio problemático)** No pudo ser eliminado. Sus datos están en `03_DATOS/gazetteer.csv`.

*   **[`/03_DATOS/`](./base_de_conocimiento/03_DATOS/)**: Todos los datos cuantitativos del proyecto.
    *   [`gazetteer.csv`](./base_de_conocimiento/03_DATOS/gazetteer.csv): El CSV consolidado con todos los datos geográficos.
    *   [`datos/crudos/`](./base_de_conocimiento/03_DATOS/datos/crudos/): Los datasets originales.
    *   [`imagenes/`](./base_de_conocimiento/03_DATOS/imagenes/): Visualizaciones y gráficos generados.

*   **[`/04_SCRIPTS/`](./base_de_conocimiento/04_SCRIPTS/)**: Todos los scripts de Python utilizados.
    *   [`consolidate_gazetteer.py`](./base_de_conocimiento/04_SCRIPTS/consolidate_gazetteer.py): Script que consolida los datos del directorio `paises`.
    *   [`scripts/`](./base_de_conocimiento/04_SCRIPTS/scripts/): Resto de scripts para descarga y análisis.

*   **[`/05_REGISTROS/`](./base_de_conocimiento/05_REGISTROS/)**: Los registros de actividad del agente.
    *   [`logs/bitacora_agente.md`](./base_de_conocimiento/05_REGISTROS/logs/bitacora_agente.md): El registro detallado de todas las acciones realizadas.

## Tareas Pendientes
Para un detalle de las tareas que no se pudieron completar, por favor consulte el archivo [`TAREAS_PENDIENTES.md`](./TAREAS_PENDIENTES.md).
