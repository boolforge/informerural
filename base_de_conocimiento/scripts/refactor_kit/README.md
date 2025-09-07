# Kit de Herramientas de Refactorización (`refactor_kit`)

**Autor:** Jules
**Propietario:** boolforge
**Propósito:** Proveer un conjunto de herramientas de línea de comandos robustas, seguras y auditables para realizar operaciones de refactorización en el repositorio `informerural`.

## Filosofía

Este kit de herramientas fue creado para mitigar la inestabilidad y falta de fiabilidad de las herramientas de entorno nativas. Cada operación está diseñada con los siguientes principios en mente:

1.  **Seguridad por Defecto:** Las operaciones destructivas (como `delete` o sobrescribir en `move`) requieren una confirmación explícita a través del flag `--force`. Las operaciones de modificación de archivos (`replace`) crean una copia de seguridad (`.bak`) por defecto.
2.  **Trazabilidad Obsesiva:** Todas las operaciones, verificaciones y errores se registran en la salida estándar (`stdout`) utilizando el módulo de `logging` de Python. Esto crea una bitácora de auditoría para cada ejecución del script.
3.  **Atomicidad:** Cada comando realiza una única acción lógica. El script se adhiere al principio de "hacer una cosa y hacerla bien".
4.  **Autocontenido:** El script `refactor.py` no tiene dependencias externas más allá de la librería estándar de Python, asegurando su portabilidad y fiabilidad en el entorno.

## Archivos

*   `refactor.py`: El script maestro que contiene toda la lógica.
*   `README.md`: Esta documentación.

## Uso General

El script se invoca desde la línea de comandos y utiliza subcomandos para cada operación.

**Sintaxis General:**
```bash
python base_de_conocimiento/scripts/refactor_kit/refactor.py <comando> [argumentos...]
```
Para obtener ayuda sobre un comando específico, usa:
```bash
python base_de_conocimiento/scripts/refactor_kit/refactor.py <comando> --help
```

### Comandos Disponibles
#### 1. move
Mueve un archivo o directorio de una ubicación a otra.

**Sintaxis:**
```bash
python refactor.py move <source> <destination> [--force]
```
**Argumentos:**
*   `source`: La ruta del archivo o directorio que quieres mover.
*   `destination`: La ruta final. Si el destino es un directorio, el `source` se moverá dentro de él. Si es una ruta de archivo, el `source` será renombrado a ese nombre.
*   `--force` (opcional): Si la ruta de destino ya existe, este flag permite sobrescribirla. Sin él, la operación se detendrá con una advertencia.

**Ejemplo:**
```bash
# Mover un archivo a un nuevo directorio, creando el directorio si no existe.
python refactor.py move base_de_conocimiento/investigacion/paises/alemania_costes_vivienda.md base_de_conocimiento/investigacion/paises/alemania/costes_vivienda.md
```

#### 2. delete
Elimina un archivo o directorio de forma permanente.

**¡ADVERTENCIA! Esta operación es destructiva e irreversible.**

**Sintaxis:**
```bash
python refactor.py delete <path> --force
```
**Argumentos:**
*   `path`: La ruta del archivo o directorio a eliminar.
*   `--force` (OBLIGATORIO): Este comando no funcionará sin el flag `--force`. Es un mecanismo de seguridad.

**Ejemplo:**
```bash
# Eliminar un archivo obsoleto
python refactor.py delete base_de_conocimiento/investigacion/temas/05_info_extraida_paramanus.md --force
```

#### 3. replace
Busca y reemplaza una cadena de texto dentro de un archivo de texto.

**Sintaxis:**
```bash
python refactor.py replace <filepath> "<old_string>" "<new_string>" [--force]
```
**Argumentos:**
*   `filepath`: La ruta del archivo que se va a modificar.
*   `<old_string>`: La cadena de texto exacta que se va a buscar.
*   `<new_string>`: El texto que reemplazará a `old_string`.
*   `--force` (opcional): Si se especifica, no se creará una copia de seguridad (`.bak`).

**Ejemplo:**
```bash
# Convertir una ruta de texto a un enlace Markdown en un archivo
python refactor.py replace base_de_conocimiento/indice.md "base_de_conocimiento/metodologia/00_directiva_filosofica.md" "[00_directiva_filosofica.md](./metodologia/00_directiva_filosofica.md)"
```
