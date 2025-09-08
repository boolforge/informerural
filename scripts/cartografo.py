import requests
import json
import os
import unicodedata
import re
import time
from concurrent.futures import ThreadPoolExecutor, TimeoutError

# --- Configuración ---
GEONAMES_USERNAME = "jfcarrb"
BASE_URL = "http://api.geonames.org/childrenJSON"
SALIDA_TEMPORAL = "salida_temporal"
CACHE_DE_API = "cache_api"
METADATOS_FILENAME = "metadatos.json"
LOG_FILE = "cartografo.log"
MAX_WORKERS = 10
# Timeout en segundos para la ejecución del script.
# Se establece un poco por debajo del timeout del entorno para permitir una salida limpia.
SCRIPT_TIMEOUT = 300

def log_message(message):
    """Escribe un mensaje en el archivo de log, con timestamp."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {message}\n")
    except Exception as e:
        print(f"Error al escribir en el log: {e}")

def normalizar_nombre(name):
    """Normaliza un string para que sea un nombre de directorio seguro."""
    nfkd_form = unicodedata.normalize('NFKD', name)
    ascii_name = "".join([c for c in nfkd_form if not unicodedata.combining(c)])
    safe_name = re.sub(r'[\s-]+', '_', ascii_name)
    safe_name = re.sub(r'[^\w_]', '', safe_name)
    return safe_name.lower()

def obtener_hijos(geoname_id):
    """Obtiene los hijos administrativos de un geonameId, usando caché."""
    cache_path = os.path.join(CACHE_DE_API, f"{geoname_id}.json")
    if os.path.exists(cache_path):
        log_message(f"Cache HIT para geonameId: {geoname_id}")
        with open(cache_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    log_message(f"Cache MISS para geonameId: {geoname_id}. Obteniendo de la API.")
    params = {'geonameId': geoname_id, 'username': GEONAMES_USERNAME}
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        if 'status' in data:
            log_message(f"Error de API para geonameId {geoname_id}: {data['status']['message']}")
            return None

        geonames_data = data.get('geonames', [])
        with open(cache_path, 'w', encoding='utf-8') as f:
            json.dump(geonames_data, f, ensure_ascii=False, indent=2)
        return geonames_data
    except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
        log_message(f"Error de red o JSON para geonameId {geoname_id}: {e}")
        return None

def procesar_division(executor, geoname_id, parent_path):
    """Procesa una división geográfica y somete a sus hijos a procesamiento en paralelo."""
    time.sleep(0.1) # Pausa para ser respetuosos con la API.
    children = obtener_hijos(geoname_id)
    if not children:
        return

    child_futures = []
    for child in children:
        feature_code = child.get('fcode', '')
        if not feature_code.startswith(('ADM', 'PPL')):
            continue

        official_name = child.get('name', 'unknown')
        if official_name == 'Castille and León':
            official_name = 'Castilla y León'

        normalized = normalizar_nombre(official_name)
        current_path = os.path.join(parent_path, normalized)

        log_message(f"Creando: {current_path}")
        os.makedirs(current_path, exist_ok=True)

        metadata = {
            "nombre_oficial": official_name,
            "geoname_id": child.get('geonameId'),
            "codigos_geograficos": {"iso_3166_2": child.get('adminCodes1', {}).get('ISO3166_2', ''), "fcode": feature_code},
            "poblacion": child.get('population'),
            "centroide": {"lat": child.get('lat'), "lon": child.get('lng')},
            "fuente_oficial": f"http://www.geonames.org/{child.get('geonameId')}"
        }
        metadata_path = os.path.join(current_path, METADATOS_FILENAME)
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)

        if feature_code.startswith('ADM'):
            # Someter la tarea hija y guardar el futuro.
            future = executor.submit(procesar_division, executor, child['geonameId'], current_path)
            child_futures.append(future)

    # Esperar a que todas las tareas hijas de este nivel se completen.
    for future in child_futures:
        future.result() # Esto propagará las excepciones de los hijos.

def main():
    """Función principal del script."""
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
    log_message("--- INICIO DE EJECUCIÓN ---")
    os.makedirs(CACHE_DE_API, exist_ok=True)
    os.makedirs(SALIDA_TEMPORAL, exist_ok=True)

    target_geoname_id = 2510769
    target_country_name = "España"
    country_path = os.path.join(SALIDA_TEMPORAL, normalizar_nombre(target_country_name))

    log_message(f"Iniciando para {target_country_name} con {MAX_WORKERS} hilos y timeout de {SCRIPT_TIMEOUT}s.")

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        root_future = executor.submit(procesar_division, executor, target_geoname_id, country_path)
        try:
            root_future.result(timeout=SCRIPT_TIMEOUT)
            log_message("¡Proceso completado en una sola ejecución!")
        except TimeoutError:
            log_message("Timeout alcanzado, como se esperaba. El progreso ha sido guardado.")
            log_message("Por favor, ejecute el script de nuevo para continuar.")
        except Exception as exc:
            log_message(f"Excepción inesperada en el futuro raíz: {exc}")

    log_message("--- FIN DE EJECUCIÓN ---")

if __name__ == "__main__":
    main()
