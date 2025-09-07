## 7. Metodología Cuantitativa (Reproducible)

*   **Normalización:** min-max robusto entre p5–p95 (clip outliers).
*   **Fusión de indicadores:** AHP (matriz 8×8, CR<0.1) para pesos base; TOPSIS para ranking final; valida con Borda y PROMETHEE (si disponible).
*   **Modelos:**
    *   Correlación (Pearson/Spearman) entre IR y resultados clínicos/proxies.
    *   Regresión: (verifica VIF, heterocedasticidad).
*   **Análisis de sensibilidad:** tornado (+/–20% pesos) y simulación Monte Carlo (1.000 corridas) sobre precios, humedad y polen.
*   **Imputación:** k-NN o MICE, marcar imputado=1.
*   **QC:** coherencia unidades, inconsistencias (p.ej., fibra=0 pero latencia ultra baja → revisar), duplicados, fechas.
*   **Caso de Estudio - Inferencia de Datos de Polen:**
    *   En zonas con estaciones locales activas (EAN/SILAM), se utilizaron los resúmenes de series temporales.
    *   En zonas sin estaciones (ej. islas remotas), se aplicó un criterio experto basado en la climatología local (ej. vientos marinos dominantes que implican baja dispersión de polen continental) para generar un índice proxy.
    *   Todos los datos inferidos o modelados de esta manera deben ser explícitamente marcados como `proxy/modelado` en cualquier dataset final para garantizar la transparencia.
