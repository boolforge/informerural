
import cdsapi
import os
import pandas as pd
import xarray as xr
import zipfile

c = cdsapi.Client()

dataset = "cams-europe-air-quality-reanalyses"
request = {
    "variable": [
        "nitrogen_dioxide",
        "ozone",
        "particulate_matter_10um",
        "particulate_matter_2.5um",
    ],
    "model": "ensemble_median",
    "level": "0",
    "date": "2022-01-01/2022-12-31",
    "time": "00:00",
    "type": "validated_reanalysis",
    "format": "netcdf",
    "area": [
        44.2, -10.0, 35.0, 5.0,  # [North, West, South, East] para España y alrededores
    ],
}

output_filename = 'copernicus_air_quality_data.zip'

try:
    print(f"Descargando datos de Copernicus con los siguientes parámetros: {request}")
    c.retrieve(
        dataset,
        request,
        output_filename
    )
    print(f"Descarga completada. Archivo guardado como {output_filename}")

    # Descomprimir y procesar el archivo
    with zipfile.ZipFile(output_filename, 'r') as zip_ref:
        zip_ref.extractall("copernicus_data")
    print("Archivo ZIP descomprimido en el directorio copernicus_data/")

    # Buscar el archivo NetCDF dentro del directorio descomprimido
    netcdf_files = [f for f in os.listdir("copernicus_data") if f.endswith(".nc")]
    if netcdf_files:
        netcdf_path = os.path.join("copernicus_data", netcdf_files[0])
        ds = xr.open_dataset(netcdf_path)
        df = ds.to_dataframe()
        print("Primeras 5 filas del DataFrame:")
        print(df.head().to_markdown(index=False, numalign="left", stralign="left"))
    else:
        print("No se encontraron archivos NetCDF en el ZIP descargado.")

except Exception as e:
    print(f"Error al descargar o procesar datos de Copernicus: {e}")


