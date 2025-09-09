# Esquema de Salida (Dataset final, todas las columnas exigidas)

## 4.1 Unidad de análisis

Fila = 1 localidad (aldea/pueblo o pequeño núcleo) dentro de una subzona rural (NUTS3/condado/comarca).

Periodo: anual (agrega series diarias/semanales al año civil indicado en anio_referencia).

## 4.2 Orden y definición de columnas (nombres exactos)

> Reglas generales de tipos
str (texto), int, float, bool (0/1 en CSV), category (valores enumerados).
Decimales con punto. Codificación UTF-8. Separador CSV = coma.

### A) Identificación geográfica y temporal

1.  **pais** (str; ISO nombre en español; ej. “Irlanda”)
2.  **region_nuts3_o_equivalente** (str; nombre oficial NUTS3/condado/comarca)
3.  **codigo_nuts3** (str; ISO/NUTS3 si aplica; ej. “IE041”; vacío si no)
4.  **subregion_local** (str; opcional; distrito/municipio si aplica)
5.  **localidad** (str; nombre oficial del núcleo)
6.  **latitud** (float; grados decimales; rango -90 a 90)
7.  **longitud** (float; grados decimales; rango -180 a 180)
8.  **altitud_m** (float; metros; ≥ -430 y ≤ 5000)
9.  **anio_referencia** (int; 2000–2100)
10. **fecha_corte_datos** (str; ISO “YYYY-MM-DD”)

### B) Índices compuestos (0–100; mayor=mejor)

11. **IR** (float) Índice Respiratorio
12. **IPSS** (float) Progresismo y Seguridad Social
13. **IAS** (float) Acceso Sanitario
14. **IAR** (float) Asequibilidad Rural
15. **ISBT** (float) Sostenibilidad y Bajo Turismo
16. **RFC** (float) Riesgo Físico-Climático (mayor = menor riesgo)
17. **ICT** (float) Conectividad y Trabajo
18. **IAC** (float) Aceptación Cultural

### C) Percentiles nacionales y globales (0–100; mayor=mejor)

19. **IR_pctl_pais** (float)
20. **IR_pctl_global** (float)
21. **IPSS_pctl_pais** (float)
... (y así sucesivamente para todos los índices)

### D) Aire, clima y alérgenos (valores anuales)

35. **pm25_ug_m3** (float; media anual; descartar si > 7 por filtro duro)
36. **pm10_ug_m3** (float; media anual)
... (y así sucesivamente)

### (El resto de las secciones del esquema de datos siguen aquí)

## 4.3 Reglas de validación clave (además de rangos)

### Filtros duros automáticos:

*   **pm25_ug_m3 > 7** ⇒ decision = "Descartar" y marcar razón en decision_motivos.
*   **humedad_relativa_pct > 75 y dew_point_c > 12** (sin microclima documentado) ⇒ “Descartar”.
*   ... (y así sucesivamente)

## 4.4 Normalización y percentiles

*   Normalización 0–1 por p5–p95 (robusta): clip a [0,1].
*   Índices entregados en 0–100 (multiplica por 100 tras ponderar).
*   Percentiles *_pctl_pais y *_pctl_global calculados por país y global.

## 4.5 Cabecera CSV (en el orden indicado)

`pais,region_nuts3_o_equivalente,codigo_nuts3,...`

## 4.6 Script: generador de plantilla + diccionario + validador

(Aquí se incluiría el código del script generador de plantillas)
