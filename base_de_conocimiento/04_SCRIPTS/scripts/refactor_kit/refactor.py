import os
import sys
import argparse
import logging
import shutil

# --- Configuración del Logging ---
# Usamos un logging detallado para auditoría, una demanda clave del usuario.
# Esto nos dará una trazabilidad completa de cada operación.
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    stream=sys.stdout # Imprimimos los logs a la salida estándar para visibilidad.
)

# --- Funciones de Lógica de Operaciones ---
# Cada función es un "wrapper" seguro alrededor de las operaciones del sistema de archivos.

def move_operation(source, destination, force=False):
    """
    Mueve un archivo o directorio. Crea directorios padres si no existen.
    Verifica paranoicamente la existencia del origen y el estado del destino.
    """
    logging.info(f"Iniciando operación de movimiento: '{source}' -> '{destination}'")
    if not os.path.exists(source):
        logging.error(f"Error Crítico: La ruta de origen no existe: {source}")
        sys.exit(1)

    if os.path.exists(destination) and not force:
        logging.warning(f"La ruta de destino ya existe: {destination}. Use --force para sobrescribir.")
        return

    try:
        # Asegurar que el directorio de destino exista
        parent_dir = os.path.dirname(destination)
        if parent_dir:
            logging.info(f"Asegurando que el directorio padre exista: {parent_dir}")
            os.makedirs(parent_dir, exist_ok=True)

        shutil.move(source, destination)
        logging.info("Movimiento completado con éxito.")

        # Verificación post-operación
        if os.path.exists(destination) and not os.path.exists(source):
             logging.info(f"VERIFICACIÓN POST-MOVIMIENTO EXITOSA: El destino '{destination}' existe y el origen '{source}' no.")
        else:
             logging.error(f"VERIFICACIÓN POST-MOVIMIENTO FALLIDA.")

    except Exception as e:
        logging.error(f"Error inesperado durante la operación de movimiento: {e}")
        sys.exit(1)

def delete_operation(path, force=False):
    """
    Elimina un archivo o directorio de forma segura.
    Requiere confirmación explícita (--force) para evitar borrados accidentales.
    """
    logging.info(f"Iniciando operación de borrado para: '{path}'")
    if not os.path.exists(path):
        logging.error(f"Error Crítico: La ruta a borrar no existe: {path}")
        sys.exit(1)

    if not force:
        logging.warning("MODO SEGURO: La operación de borrado requiere el flag --force.")
        logging.warning(f"Para borrar '{path}', ejecute de nuevo el comando con --force.")
        sys.exit(1)

    try:
        if os.path.isdir(path):
            shutil.rmtree(path)
            logging.info(f"Directorio '{path}' y su contenido han sido eliminados.")
        else:
            os.remove(path)
            logging.info(f"Archivo '{path}' ha sido eliminado.")

        if not os.path.exists(path):
            logging.info(f"VERIFICACIÓN POST-BORRADO EXITOSA: La ruta '{path}' ya no existe.")
        else:
            logging.error(f"VERIFICACIÓN POST-BORRADO FALLIDA: La ruta '{path}' todavía existe.")

    except Exception as e:
        logging.error(f"Error inesperado durante la operación de borrado: {e}")
        sys.exit(1)

def replace_text_operation(filepath, old_string, new_string, force=False):
    """
    Reemplaza texto dentro de un archivo.
    Por defecto, realiza una copia de seguridad.
    """
    logging.info(f"Iniciando operación de reemplazo de texto en: '{filepath}'")
    if not os.path.isfile(filepath):
        logging.error(f"Error Crítico: La ruta especificada no es un archivo: {filepath}")
        sys.exit(1)

    backup_path = f"{filepath}.bak"
    if not force:
        logging.info(f"MODO SEGURO: Creando copia de seguridad en: {backup_path}")
        shutil.copy2(filepath, backup_path)

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if old_string not in content:
            logging.warning(f"La cadena a reemplazar no fue encontrada en el archivo: '{old_string}'")
            return

        new_content = content.replace(old_string, new_string)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        logging.info("Reemplazo de texto completado con éxito.")
        logging.info(f"VERIFICACIÓN POST-REEMPLAZO: Por favor, revise el contenido de '{filepath}' manualmente.")

    except Exception as e:
        logging.error(f"Error inesperado durante la operación de reemplazo: {e}")
        sys.exit(1)


# --- Función Principal (Controlador de Comandos) ---

def main():
    """
    Función principal que parsea los argumentos y llama a la operación correspondiente.
    """
    parser = argparse.ArgumentParser(
        description="Kit de Herramientas de Refactorización para el repositorio informerural.",
        epilog="Diseñado por Jules para boolforge. Use 'python refactor.py <comando> --help' para más información."
    )
    subparsers = parser.add_subparsers(dest='command', required=True, help='Comando a ejecutar')

    # Sub-parser para 'move'
    parser_move = subparsers.add_parser('move', help='Mueve un archivo o directorio.')
    parser_move.add_argument('source', type=str, help='Ruta de origen.')
    parser_move.add_argument('destination', type=str, help='Ruta de destino.')
    parser_move.add_argument('--force', action='store_true', help='Fuerza la sobreescritura si el destino ya existe.')
    parser_move.set_defaults(func=lambda args: move_operation(args.source, args.destination, args.force))

    # Sub-parser para 'delete'
    parser_delete = subparsers.add_parser('delete', help='Elimina un archivo o directorio (requiere --force).')
    parser_delete.add_argument('path', type=str, help='Ruta a eliminar.')
    parser_delete.add_argument('--force', action='store_true', help='Confirmación explícita para borrar.')
    parser_delete.set_defaults(func=lambda args: delete_operation(args.path, args.force))

    # Sub-parser para 'replace'
    parser_replace = subparsers.add_parser('replace', help='Reemplaza texto en un archivo.')
    parser_replace.add_argument('filepath', type=str, help='Ruta del archivo a modificar.')
    parser_replace.add_argument('old_string', type=str, help='Texto a buscar.')
    parser_replace.add_argument('new_string', type=str, help='Texto nuevo.')
    parser_replace.add_argument('--force', action='store_true', help='No crea copia de seguridad.')
    parser_replace.set_defaults(func=lambda args: replace_text_operation(args.filepath, args.old_string, args.new_string, args.force))

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
