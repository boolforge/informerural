## 2. Fuentes de Datos (Priorizar oficiales, últimas ediciones)

### A. Fuentes de Datos Generales

*   **Salud/Aire/Clima:** OMS/WHO, EEA (Air Quality), Copernicus (CAMs), ERA5 (humedad/temperatura/dew point), NOAA/KNMI/MetOffice/Met Éireann, pollen calendars (EAACI, universidades), radón (mapas nacionales), incendios (Copernicus EFFIS), HDD/CDD.
*   **Socio-político:** Eurostat, OECD, World Justice Project, Transparency International, registros de delitos de odio, participación y voto por sección (estadística electoral) para medir auge/descenso de extrema derecha local.
*   **Economía y Vivienda:** Estadísticas nacionales de precio de suelo rústico (€/ha), precio vivienda (€/m² y alquiler), renta mediana, impuestos y tasas (IBI/Grundsteuer/etc.).
*   **Accesos y Servicios:** OpenStreetMap/oficiales para tiempos a hospitales, densidad sanitaria (médicos/1.000), fibra/5G (reguladores telecom), cooperativas agro y mercados locales.
*   **Turismo y Presión:** Pernoctaciones/residente, densidad Airbnb/Booking, estacionalidad, cruceros (puertos) y capacidad de carga local.
*   **Ambiente y Riesgos:** Inundabilidad (mapas hidrográficos), seísmo (servicios geológicos), deslizamientos, sequía (SPEI), ruido (directiva europea), luz (VIIRS), nitrógeno/amoníaco (agricultura intensiva).
*   **Regla de calidad:** Cita todas las métricas con fuente/año; prohíbe suposiciones sin respaldo; documenta imputación/normalización.

### B. Inventario de Fuentes de Datos de Polen (Ejemplos)

He localizado los servicios y portales clave para las zonas de tu shortlist; para cada uno indico si tienen datos públicos y cómo acceder:

*   **European Aeroallergen Network (EAN) / polleninfo.org** — Portal de gráficos públicos (Flow Charts). Datos por estación: gráficos públicos; CSV/históricos: acceso por membresía o solicitud. Soporte: support@polleninfo.eu.
    *   URL: https://ean.polleninfo.eu/Ean/

*   **SILAM / EPR (European Pollen Reanalysis)** — reanálisis 1980–2022 para Betula/Alnus/Olea; ideal para extracción por coordenada (NetCDF). Público en artículos y repositorios (Copernicus / Nature data references). Necesitas descargar ficheros NetCDF y extraer con xarray.

*   **Iceland — Natural Science Institute / NATT (NSII)** — tienen monitoring nacional y previsiones; algunos datos históricos accesibles; página con información y contacto para series. Útil para Húsavík, Egilsstaðir, Westfjords.

*   **Finland — Norkko / University of Turku / Finnish Meteorological Institute (FMI)** — servicio de aerobiología con series; estaciones EAN registradas (Kuhmo y Carelia cercano). Frecuentemente permite descarga o suministro bajo petición.

*   **UK — Met Office / Local Councils** — Met Office publica previsiones (5 días) y algunos datos; muchas estaciones EAN del Reino Unido publican en polleninfo o en portales locales (p.ej. Scottish pollen monitoring). Orkney Council y Met Office ofrecen previsiones; algunas series deben solicitarse.

*   **Sweden — SMHI (Swedish Meteorological) / EAN** — SMHI dispone de datos y mapas; estaciones EAN en Jämtland pueden tener series.

*   **Norway — MET Norway / SILAM** — MET Norway coopera con SILAM y publica pronósticos; estaciones locales pueden ofrecer datos.
