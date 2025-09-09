## 3. Indicadores y Definición Operativa (con Fórmulas)

Normaliza a 0–1 cada variable (↑ bueno, ↓ malo), min-max robusto (p5–p95) y combina con pesos:

### 3.1 Índice Respiratorio (IR, 0–100; mayor=mejor)

*   **Métricas:** PM₂.₅ anual (↓), PM₁₀ anual (↓), NO₂ (↓), O₃ máximos 8h (↓), días humo/incendio (↓), humedad relativa media (↓), dew point anual (↓).
*   **Análisis Profundo de Alérgenos:** Polen index por taxa (↓: abedul, artemisia, ambrosía, ciprés, olivo, cedro japonés), mold index (↓), inversiones térmicas (↓).
*   **Radón:** (↓; descartar > nivel de referencia nacional).
*   **Fórmula (ej.):** Índice Respiratorio = w₁*(1-PM₂.₅_norm) + w₂*(1-HR_norm) + w₃*(1-Pollen_norm)

### 3.2 Índice de Progresismo y Seguridad Social (IPSS, 0–100)

*   **Métricas:** Crimen total (↓), delitos de odio (↓), voto/extrema derecha (↓ y tendencia ↓), WJP Rule of Law (↑), protecciones LGTBI+ (↑), libertad religiosa y minorías (↑), gasto social/PIB (↑), densidad de servicios sociales (↑).

### 3.3 Índice de Acceso Sanitario (IAS, 0–100)

*   **Métricas:** Tiempo isócrona a urgencias (↓), hospitales/100k (↑), neumología disponible (↑), camas UCI/100k (↑), telemedicina (↑), listas de espera (↓).
*   **Análisis Profundo del Sistema Integral:** Tiempos de espera REALES para especialistas y cirugías. Ratio de profesionales por habitante (médicos, psicólogos/psiquiatras especializados en TDAH/TLP, pediatras, geriatras, alergólogos e inmunólogos). Coste de copagos y seguros privados. Tasa de suicidios. ¿El sistema se enfoca en prevención o solo en tratamiento? ¿Hay programas de salud comunitaria y apoyo a la salud mental accesibles y de calidad?

### 3.4 Índice de Asequibilidad Rural (IAR, 0–100)

*   **Métricas:** €/ha suelo rústico (↓), €/m² compra (↓), €/mes alquiler (↓), carga vivienda % renta (↓), impuestos y tasas (↓), coste cesta vegana local (↓).

### 3.5 Índice de Sostenibilidad y Bajo Turismo (ISBT, 0–100)

*   **Métricas:** Residuos reciclados % (↑), renovables % (↑), Airbnb/residente (↓), pernoctaciones/residente (↓), capacidad de carga/uso (↓), ruido (↓), luz nocturna (↓).

### 3.6 Riesgo Físico-Climático (RFC, 0–100; mayor=menos riesgo)

*   **Métricas:** Inundación, sequía (SPEI), incendios, seísmo, deslizamientos, olas de calor (todos invertidos y agregados).

### 3.7 Conectividad y Trabajo (ICT, 0–100)

*   **Métricas:** Cobertura fibra (↑), 5G (↑), latencia y ancho de banda (↑), espacios de cowork rural (↑), fiabilidad eléctrica (↑).

### 3.8 Índice de Aceptación Cultural (IAC, 0–100)

*   **Métricas:** Actitudes LGTBI (↑), vegan-friendly (↑: tiendas, mercados, restaurantes), laicidad/respeto minorías (↑), conflictividad comunitaria (↓).
*   **Análisis Profundo de la Cohesión:** ¿Cómo se integran los recién llegados? Disponibilidad y calidad de servicios de asistencia social (comedores, ayuda a domicilio, programas de reinserción y lucha contra adicciones).

### Ponderación MCDA (base, ajustable AHP/TOPSIS):

*   IR 22%, IPSS 15%, IAS 14%, IAR 14%, ISBT 10%, RFC 10%, ICT 8%, IAC 7%.
*   Entrega matriz AHP (pareada) + consistency ratio. Ejecuta análisis de sensibilidad ±20% en pesos.
