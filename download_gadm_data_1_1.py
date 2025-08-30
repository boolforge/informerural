import pygadm
import pandas as pd
import os

# Mapeo de nombres de países a códigos ISO 3166-1 alpha-3
country_iso_map = {
    'Ireland': 'IRL',
    'United Kingdom': 'GBR',
    'Iceland': 'ISL',
    'Norway': 'NOR',
    'Sweden': 'SWE',
    'Finland': 'FIN',
    'Denmark': 'DNK',
    'Netherlands': 'NLD',
    'Belgium': 'BEL',
    'Luxembourg': 'LUX',
    'Switzerland': 'CHE',
    'Austria': 'AUT',
    'Germany': 'DEU',
    'New Zealand': 'NZL',
    'Japan': 'JPN'
}

# Lista de países a descargar (extraída de paramanus.txt)
countries = [
    'Ireland', 'United Kingdom', 'Iceland', 'Norway', 'Sweden', 'Finland',
    'Denmark', 'Netherlands', 'Belgium', 'Luxembourg', 'Switzerland', 'Austria',
    'Germany', 'New Zealand', 'Japan'
]

output_dir = '/home/ubuntu/project/inputs'
os.makedirs(output_dir, exist_ok=True)

for country_name in countries:
    iso_code = country_iso_map.get(country_name)
    if not iso_code:
        print(f"Código ISO no encontrado para {country_name}. Saltando.")
        continue

    print(f"Descargando datos GADM para {country_name} ({iso_code})...")
    try:
        # pygadm.get_data descarga el nivel más detallado por defecto
        # La documentación sugiere que el nivel 0 es el país, y niveles superiores son subdivisiones.
        # Para obtener el máximo detalle, no especificamos el nivel, o usamos el nivel más alto disponible.
        # La librería pygadm automáticamente descarga el nivel más detallado disponible.
        gdf = pygadm.get_data(code=iso_code)
        output_path = os.path.join(output_dir, f"gadm_{iso_code}.gpkg")
        gdf.to_file(output_path, driver="GPKG")
        print(f"Datos para {country_name} guardados en {output_path}")
    except Exception as e:
        print(f"Error al descargar o guardar datos para {country_name}: {e}")

print("Proceso de descarga de GADM completado.")


