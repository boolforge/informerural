
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


