#!/usr/bin/env python3
# Requiere: requests, beautifulsoup4, pandas
# Objetivo: para una lista de URLs de estación/página (polleninfo.org o nacional) descargar gráficos/puntos de datos (si la web expone series JSON o SVG con datapoints).
# NOTA: EAN no da CSV directo en público en muchos casos; este script intenta extraer datos visibles en la página.

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from datetime import datetime

def extract_from_polleninfo(url):
    # ejemplo: https://www.polleninfo.org/flow-charts/.... (cambiar según estación)
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    # buscar scripts con datos JSON incrustados o tags <svg> con 'data-values'
    # esto varía entre implementaciones; intentamos heurísticos:
    data = []
    # buscar scripts con "chart" o "data"
    for script in soup.find_all("script"):
        txt = script.string
        if not txt:
            continue
        if 'series' in txt or 'data' in txt:
            # regex búsqueda de arrays numéricos
            m = re.findall(r'\[[-\d,.\s]+\]', txt)
            for arr in m:
                try:
                    nums = [float(x) for x in re.findall(r'[-]?\d+\.?\d*', arr)]
                    if len(nums) > 10:
                        data.append(nums)
                except:
                    pass
    # devolvemos data bruto (posible limpieza manual)
    return data

# ejemplo de uso
if __name__ == '__main__':
    stations = {
        "Husavik_Iceland": "https://www.polleninfo.org/flow-charts/...."  # sustituir URL exacta de estación
    }

    all_dfs = {}
    for name, url in stations.items():
        try:
            raw = extract_from_polleninfo(url)
            # transformar raw en dataframe según formato detectado (depende de sitio)
            df = pd.DataFrame(raw).T
            all_dfs[name] = df
        except Exception as e:
            print("Error:", name, e)

    # Guardar CSVs
    for name, df in all_dfs.items():
        df.to_csv(f"{name}_pollen_scraped.csv", index=False)
