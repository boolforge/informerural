
#!/usr/bin/env python3
"""
Script para analizar y comparar datos de calidad del aire de múltiples sitios de Londres.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

# Cargar el archivo CSV consolidado
file_path = \'/home/ubuntu/london_air_quality_multiple_sites.csv\'

try:
    df = pd.read_csv(file_path)
    print(f"Datos cargados exitosamente. Filas: {len(df)}, Columnas: {len(df.columns)}")
except FileNotFoundError:
    print(f"Error: El archivo {file_path} no fue encontrado.")
    exit()
except Exception as e:
    print(f"Error al cargar el archivo: {e}")
    exit()

# Preprocesamiento de datos
# Convertir la columna \'MeasurementDateGMT\' a formato de fecha y hora
df[\'MeasurementDateGMT\'] = pd.to_datetime(df[\'MeasurementDateGMT\'], errors=\'coerce\')

# Eliminar filas con fechas nulas
df.dropna(subset=[\'MeasurementDateGMT\'], inplace=True)

# Establecer \'MeasurementDateGMT\' como índice
df.set_index(\'MeasurementDateGMT\', inplace=True)

# Extraer nombres de contaminantes y renombrar columnas
# Las columnas tienen el formato "Site Name: Pollutant Name (Unit)"
# Queremos solo "Pollutant Name"

new_columns = {}
pollutant_names = set()
for col in df.columns:
    match = re.search(r\':\\s*(.*?)\\s*\\(\', col)
    if match:
        pollutant_name = match.group(1).replace(\' Particulate\', \'\') # Eliminar \' Particulate\'
        new_columns[col] = pollutant_name
        pollutant_names.add(pollutant_name)
    elif col in [\'Site\', \'Units\']:
        new_columns[col] = col

df.rename(columns=new_columns, inplace=True)

# Asegurarse de que solo las columnas que existen en el DataFrame se incluyan en pollutant_cols
pollutant_cols = [p for p in pollutant_names if p in df.columns and p != \'Site\'] # Excluir \'Site\' de los contaminantes

# Convertir columnas de contaminantes a numérico, forzando errores a NaN
for col in pollutant_cols:
    # Convertir a string primero para evitar el TypeError si la columna es de tipo object con valores mixtos
    df[col] = pd.to_numeric(df[col].astype(str), errors=\'coerce\')

print("Columnas de contaminantes identificadas:", pollutant_cols)

# Calcular medias diarias y mensuales por sitio y contaminante
daily_mean = df.groupby([df.index.date, \'Site\'])[pollutant_cols].mean()
daily_mean.index.names = [\'Date\', \'Site\']
daily_mean.to_csv(\'/home/ubuntu/london_air_quality_daily_mean_multi_site.csv\')
print("Medias diarias calculadas y guardadas.")

monthly_mean = df.groupby([df.index.to_period(\'M\'), \'Site\'])[pollutant_cols].mean()
monthly_mean.index.names = [\'Month\', \'Site\']
monthly_mean.to_csv(\'/home/ubuntu/london_air_quality_monthly_mean_multi_site.csv\')
print("Medias mensuales calculadas y guardadas.")

# Calcular percentiles (p90, p95) para contaminantes clave por sitio
percentiles_data = {}
for site in df[\'Site\'].unique():
    site_df = df[df[\'Site\'] == site]
    percentiles_data[site] = {
        \'PM10_p90\': site_df[\'PM10\'].quantile(0.90) if \'PM10\' in site_df.columns else None,
        \'PM2.5_p90\': site_df[\'PM2.5\'].quantile(0.90) if \'PM2.5\' in site_df.columns else None,
        \'NO2_p90\': site_df[\'NO2\'].quantile(0.90) if \'NO2\' in site_df.columns else None,
        \'O3_p90\': site_df[\'O3\'].quantile(0.90) if \'O3\' in site_df.columns else None
    }
percentiles_df = pd.DataFrame.from_dict(percentiles_data, orient=\'index\')
percentiles_df.index.name = \'Site\'

percentiles_df.to_csv(\'/home/ubuntu/london_air_quality_percentiles_multi_site.csv\')
print("Percentiles calculados y guardados.")

# Evaluación de cumplimiento de objetivos (ejemplo para PM10 y NO2)
compliance_data = {}
for site in df[\'Site\'].unique():
    site_df = df[df[\'Site\'] == site]
    
    pm10_mean = site_df[\'PM10\'].mean() if \'PM10\' in site_df.columns else None
    no2_mean = site_df[\'NO2\'].mean() if \'NO2\' in site_df.columns else None
    
    compliance_data[site] = {
        \'PM10_Mean\': pm10_mean,
        \'PM10_Compliance\': \'Cumple\' if pm10_mean and pm10_mean <= 50 else \'No Cumple\',
        \'NO2_Mean\': no2_mean,
        \'NO2_Compliance\': \'Cumple\' if no2_mean and no2_mean <= 40 else \'No Cumple\'
    }
compliance_df = pd.DataFrame.from_dict(compliance_data, orient=\'index\')
compliance_df.index.name = \'Site\'

compliance_df.to_csv(\'/home/ubuntu/london_air_quality_compliance_multi_site.csv\')
print("Evaluación de cumplimiento guardada.")

# Generación de gráficos comparativos

# Gráfico de tendencias diarias de PM10 para múltiples sitios
if \'PM10\' in pollutant_cols:
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=daily_mean.reset_index(), x=\'Date\', y=\'PM10\', hue=\'Site\')
    plt.title(\'Tendencia Diaria de PM10 en Múltiples Sitios de Londres\')
    plt.xlabel(\'Fecha\')
    plt.ylabel(\'PM10 (ug/m3)\')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(\'/home/ubuntu/pm10_daily_trend_multi_site.png\')
    plt.close()
    print("Gráfico de tendencia diaria de PM10 generado.")

# Gráfico de barras de medias mensuales de NO2 por sitio
if \'NO2\' in pollutant_cols:
    plt.figure(figsize=(12, 6))
    sns.barplot(data=monthly_mean.reset_index(), x=\'Site\', y=\'NO2\')
    plt.title(\'Media Mensual de NO2 por Sitio en Londres\')
    plt.xlabel(\'Sitio\')
    plt.ylabel(\'NO2 (ug/m3)\')
    plt.tight_layout()
    plt.savefig(\'/home/ubuntu/no2_monthly_mean_multi_site.png\')
    plt.close()
    print("Gráfico de media mensual de NO2 generado.")

# Gráfico de barras de cumplimiento de PM2.5 por sitio (percentil 90)
if \'PM2.5\' in pollutant_cols:
    plt.figure(figsize=(12, 6))
    sns.barplot(data=percentiles_df.reset_index(), x=\'Site\', y=\'PM2.5_p90\')
    plt.title(\'Percentil 90 de PM2.5 por Sitio en Londres\')
    plt.xlabel(\'Sitio\')
    plt.ylabel(\'PM2.5 (ug/m3)\')
    plt.tight_layout()
    plt.savefig(\'/home/ubuntu/pm25_p90_multi_site.png\')
    plt.close()
    print("Gráfico de percentil 90 de PM2.5 generado.")

print("Análisis completado. Archivos y gráficos generados.")




