import requests
import pandas as pd
import pyarrow.parquet as pq
import io

# Países de interés (códigos de la API de la EEA)
countries = [
    'DE', 'FR', 'IT', 'DK', 'IE', 'LU', 'CH', 'GB', 'IS', 'NO', 'SE', 'FI', 'NL', 'BE', 'AT'
    # Nueva Zelanda y Japón no están en la lista de países de la EEA, se buscarán otras fuentes para ellos.
]

# Contaminantes de interés (IDs de la API de la EEA)
pollutants = {
    'PM2.5': 'http://dd.eionet.europa.eu/vocabulary/aq/pollutant/5',
    'PM10': 'http://dd.eionet.europa.eu/vocabulary/aq/pollutant/106',
    'NO2': 'http://dd.eionet.europa.eu/vocabulary/aq/pollutant/8',
    'O3': 'http://dd.eionet.europa.eu/vocabulary/aq/pollutant/7'
}

# URL del endpoint de descarga dinámica
download_url = "https://eeadmz1-downloads-api-appservice.azurewebsites.net/ParquetFile/dynamic"

# Rango de fechas (desde 2013, como indica la documentación de la EEA)
date_time_start = "2013-01-01T00:00:00Z"
date_time_end = "2025-08-30T23:59:59Z" # Fecha actual

# Tipo de agregación (ej. anual, diario, horario - se usará 'daily' para empezar)
aggregation_type = "daily"

# Correo electrónico (requerido por la API)
email = "test@example.com"

all_data = pd.DataFrame()

for country_code in countries:
    for pollutant_name, pollutant_id in pollutants.items():
        print(f"Descargando datos para {country_code} - {pollutant_name}...")

        payload = {
            "countries": [country_code],
            "pollutants": [pollutant_id],
            "dataset": 0, # 0 para datos verificados y actualizados
            "source": "All", # Opcional, se puede especificar una fuente si se conoce
            "method": "All", # Opcional
            "dateTimeStart": date_time_start,
            "dateTimeEnd": date_time_end,
            "aggregationType": aggregation_type,
            "email": email
        }

        headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(download_url, json=payload, headers=headers)
            response.raise_for_status() # Lanza una excepción para códigos de estado HTTP erróneos

            # La API devuelve un archivo Parquet directamente en la respuesta
            parquet_file = io.BytesIO(response.content)
            table = pq.read_table(parquet_file)
            df = table.to_pandas()

            # Añadir columnas de país y contaminante para identificar los datos
            df['country'] = country_code
            df['pollutant'] = pollutant_name

            all_data = pd.concat([all_data, df], ignore_index=True)
            print(f"Datos de {country_code} - {pollutant_name} descargados y procesados.")

        except requests.exceptions.RequestException as e:
            print(f"Error al descargar datos para {country_code} - {pollutant_name}: {e}")
        except Exception as e:
            print(f"Error al procesar datos para {country_code} - {pollutant_name}: {e}")

# Guardar todos los datos en un único archivo CSV
if not all_data.empty:
    output_file = "eea_air_quality_data.csv"
    all_data.to_csv(output_file, index=False)
    print(f"Todos los datos descargados y guardados en {output_file}")
else:
    print("No se pudieron descargar datos.")


\n\n--- Contenido de archivo original: download_eea_air_quality_1.py, download_eea_air_quality_4.py, download_eea_air_quality_5.py, download_eea_air_quality_6.py, download_eea_air_quality.py, download_eea_air_quality_2_2.py, download_eea_air_quality_2_1.py, download_eea_air_quality_2.py, download_eea_air_quality_3.py ---\n\n
import requests
import json
import pyarrow.parquet as pq
import pandas as pd
import io
import zipfile
import os

# URL del endpoint de la API
url = "https://eeadmz1-downloads-api-appservice.azurewebsites.net/ParquetFile/dynamic"

# Cuerpo de la solicitud basado en la documentación de la API
payload = {
    "countries": ["ES"],  # Volviendo a España para la prueba
    "cities": [],
    "pollutants": ["PM2.5", "PM10", "NO2", "O3"],  # Notación de cadena para los contaminantes
    "dataset": 2, # Cambiado a dataset 2 (Unverified data from 2024)
    "source": "", # Dejando vacío para ver si es un problema de formato
    "method": "", # Dejando vacío para ver si es un problema de formato
    "dateTimeStart": "2024-01-01T00:00:00.000Z", # Fecha de inicio (ejemplo: 2024)
    "dateTimeEnd": "2024-12-31T23:59:59.999Z",   # Fecha de fin (ejemplo: 2024)
    "aggregationType": "day", # Corregido a 'day' según el mensaje de error
    "email": "test@example.com" # Correo electrónico para la descarga
}

headers = {
    'Content-Type': 'application/json'
}

print(f"Enviando solicitud a: {url}")
print(f"Con payload: {json.dumps(payload, indent=2)}")

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(f"Código de estado: {response.status_code}")

if response.status_code == 200:
    try:
        # Guardar el contenido binario como un archivo ZIP
        zip_filename = "eea_air_quality_data.zip"
        with open(zip_filename, "wb") as f:
            f.write(response.content)
        print(f"Archivo {zip_filename} guardado exitosamente.")

        # Extraer el contenido del archivo ZIP
        with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
            # Asumimos que hay un solo archivo Parquet en el ZIP
            parquet_filename_in_zip = zip_ref.namelist()[0]
            zip_ref.extractall()
            print(f"Archivo {parquet_filename_in_zip} extraído exitosamente.")

        # Construir la ruta completa al archivo Parquet extraído
        extracted_parquet_path = os.path.join(os.getcwd(), parquet_filename_in_zip)

        # Leer el archivo Parquet y mostrar las primeras filas
        table = pq.read_table(extracted_parquet_path)
        df = table.to_pandas()
        print("Primeras 5 filas del DataFrame:")
        print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
else:
    print(f"Error en la solicitud. Respuesta: {response.text}")
