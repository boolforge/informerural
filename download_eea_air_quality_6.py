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


