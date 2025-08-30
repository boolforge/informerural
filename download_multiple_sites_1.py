#!/usr/bin/env python3
"""
Script para descargar datos de calidad del aire de múltiples sitios de Londres
usando la API de London Air Quality Network
"""

import requests
import pandas as pd
import time
from datetime import datetime, timedelta

# Lista de sitios de monitoreo activos conocidos
sites = [
    'BL0',  # Camden - Bloomsbury
    'MY1',  # Westminster - Marylebone Road
    'KC1',  # Kensington and Chelsea - North Kensington
    'TH4',  # Tower Hamlets - Blackwall
    'CR8',  # Croydon - Norbury
    'BX1',  # Bexley - Belvedere
    'HV1',  # Havering - Rainham
    'RB7',  # Redbridge - Ley Street
    'WM0',  # Westminster - Oxford Street
    'LW2'   # Lewisham - New Cross
]

# Fechas para el último mes
end_date = datetime.now()
start_date = end_date - timedelta(days=30)

base_url = "https://api.erg.ic.ac.uk/AirQuality/Data/Site/Wide/SiteCode={}/StartDate={}/EndDate={}/csv"

all_data = []

print("Descargando datos de calidad del aire para múltiples sitios...")

for site in sites:
    try:
        url = base_url.format(
            site,
            start_date.strftime('%Y-%m-%d'),
            end_date.strftime('%Y-%m-%d')
        )
        
        print(f"Descargando datos para sitio {site}...")
        response = requests.get(url, timeout=30)
        
        if response.status_code == 200 and len(response.text) > 100:
            # Guardar datos individuales
            filename = f"/home/ubuntu/air_data_{site}.csv"
            with open(filename, 'w') as f:
                f.write(response.text)
            
            # Procesar datos para análisis
            lines = response.text.strip().split('\n')
            if len(lines) > 1:
                # Leer como DataFrame
                from io import StringIO
                df = pd.read_csv(StringIO(response.text))
                df['Site'] = site
                all_data.append(df)
                print(f"✓ Datos descargados para {site}: {len(df)} registros")
            else:
                print(f"✗ Sin datos válidos para {site}")
        else:
            print(f"✗ Error descargando {site}: {response.status_code}")
            
        # Pausa entre solicitudes
        time.sleep(1)
        
    except Exception as e:
        print(f"✗ Error con sitio {site}: {str(e)}")

# Consolidar todos los datos
if all_data:
    combined_df = pd.concat(all_data, ignore_index=True)
    combined_df.to_csv('/home/ubuntu/london_air_quality_multiple_sites.csv', index=False)
    print(f"\n✓ Datos consolidados guardados: {len(combined_df)} registros totales")
    
    # Resumen por sitio
    print("\nResumen por sitio:")
    site_summary = combined_df.groupby('Site').size()
    for site, count in site_summary.items():
        print(f"  {site}: {count} registros")
else:
    print("✗ No se pudieron descargar datos de ningún sitio")

print("Proceso completado.")



