#!/usr/bin/env python3
# Requiere: xarray, netCDF4, pandas, numpy, pyproj
# Entrada: NetCDF EPR file(s) con variable 'betula' y 'grass' (units: grains/m3) - daily or hourly
# Entrada2: csv con localidades: Localidad, Lat, Lon
# Salida: CSV con time series y métricas (median seasonal, p95, days > threshold)

import xarray as xr
import pandas as pd
import numpy as np
from pyproj import Transformer
from math import radians

def nearest_gridpoint(ds, lat, lon):
    # encontrar índice de lat/lon más cercano
    absdiff = np.abs(ds.lat - lat) + np.abs(ds.lon - lon)
    idx = absdiff.argmin().values
    # convertir index a index2d (si necesario)
    iy = int(np.argmin(np.abs(ds.lat - lat)))
    ix = int(np.argmin(np.abs(ds.lon - lon)))
    return iy, ix

def main():
    # config
    netcdf_path = "epr_betula_grass_1980_2022_daily.nc"  # ruta al netCDF consolidado
    locations_csv = "localidades_coords.csv"  # tu listado: Localidad,Lat,Lon

    # cargar
    try:
        ds = xr.open_dataset(netcdf_path)  # variables: betula, grass; dims: time, lat, lon
        locs = pd.read_csv(locations_csv)
    except FileNotFoundError as e:
        print(f"Error: Archivo no encontrado - {e}. Asegúrate de que los archivos de entrada existen.")
        return

    results = []
    for _, row in locs.iterrows():
        loc = row['Localidad']
        lat = row['Lat']
        lon = row['Lon']
        iy, ix = nearest_gridpoint(ds, lat, lon)
        betula_ts = ds['betula'][:, iy, ix].to_series()  # daily series
        grass_ts = ds['grass'][:, iy, ix].to_series()

        # Calcular métricas
        betula_median = betula_ts.median()
        betula_p95 = betula_ts.quantile(0.95)
        betula_days_over_50 = (betula_ts > 50).sum()

        grass_median = grass_ts.median()
        grass_p95 = grass_ts.quantile(0.95)
        grass_days_over_50 = (grass_ts > 50).sum()

        results.append({
            "Localidad": loc,
            "Betula_median_grains_m3": betula_median,
            "Betula_p95_grains_m3": betula_p95,
            "Betula_days_over_50_grains_m3": betula_days_over_50,
            "Grass_median_grains_m3": grass_median,
            "Grass_p95_grains_m3": grass_p95,
            "Grass_days_over_50_grains_m3": grass_days_over_50,
            "Pollen_Estimate_Source": "SILAM reanalysis (expert-estimate)"
        })

    final_df = pd.DataFrame(results)
    final_df.to_csv("pollen_numeric_estimates_silam.csv", index=False)
    print("Terminado: pollen_numeric_estimates_silam.csv")

if __name__ == '__main__':
    main()
