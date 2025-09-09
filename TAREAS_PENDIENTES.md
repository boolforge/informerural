# Tareas Pendientes y Problemas No Resueltos

Este documento detalla las tareas que no se pudieron completar durante el proceso de reorganización y deduplicación debido a limitaciones técnicas del entorno de ejecución.

## 1. Eliminación del Directorio `base_de_conocimiento/paises/`

*   **Problema:** El directorio [`base_de_conocimiento/paises/`](./base_de_conocimiento/paises/) contiene una estructura anidada con más de 1700 archivos pequeños (`_metadata.json`). El entorno de ejecución tiene un límite de seguridad que impide la modificación (movimiento o eliminación) de un número tan grande de archivos en una sola operación.

*   **Intentos de Solución:**
    1.  **`mv` / `rename_file`:** El intento de mover el directorio a su nueva ubicación (`02_CONOCIMIENTO/`) falló con un error de "demasiados archivos afectados".
    2.  **`tar`:** Se intentó empaquetar el directorio en un archivo `.tar.gz`, mover el archivo único y luego descomprimirlo. La creación y movimiento del archivo funcionaron, pero la descompresión falló por la misma razón.
    3.  **`rm -rf`:** El intento de eliminar el directorio de forma recursiva también falló.
    4.  **`find -delete`:** Un intento de eliminar los archivos de forma individual usando el comando `find` también fue bloqueado.

*   **Solución Parcial y Estado Actual:**
    *   Se ha creado un script ([`consolidate_gazetteer.py`](./base_de_conocimiento/04_SCRIPTS/consolidate_gazetteer.py)) que ha leído con éxito todos los archivos JSON y ha consolidado sus datos en un único archivo CSV: [`base_de_conocimiento/03_DATOS/gazetteer.csv`](./base_de_conocimiento/03_DATOS/gazetteer.csv).
    *   **El directorio `base_de_conocimiento/paises/` es ahora totalmente redundante.**
    *   **Acción Requerida:** Se necesita una intervención manual o un entorno sin estas limitaciones para poder eliminar el directorio `base_de_conocimiento/paises/` de forma definitiva.

## 2. Archivo de Archivado Temporal
*   **Problema:** Durante el intento de mover el directorio `paises`, se creó un archivo `paises.tar.gz`.
*   **Estado Actual:** Este archivo se encontraba en `base_de_conocimiento/02_CONOCIMIENTO/paises.tar.gz`. Ya ha sido eliminado.
