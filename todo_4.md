## Tareas Pendientes

### Fase 1: Análisis y comprensión profunda del protocolo de investigación
- [x] Leer y comprender el protocolo de investigación detallado.
- [x] Identificar todos los criterios de inclusión y exclusión de países y regiones.
- [x] Entender los arquetipos de usuario y el perfil de necesidades personales.
- [x] Listar todos los productos finales requeridos (informe, datos, gráficos).
- [x] Revisar las fuentes de datos priorizadas.
- [x] Comprender los indicadores y sus definiciones operativas, incluyendo fórmulas y ponderaciones.
- [x] Anotar los criterios de descarte duros (filtros).
- [x] Entender la cobertura geográfica y los mínimos de subzonas/localidades.
- [x] Familiarizarse con el esquema de salida del dataset.
- [x] Comprender la metodología cuantitativa (normalización, fusión, análisis de sensibilidad, imputación, QC).
- [x] Revisar las reglas específicas respiratorias.
- [x] Entender el proceso de selección final y narrativa.

### Fase 2: Recopilación de datos macro-contextuales y socio-políticos por país
- [x] Investigar y recopilar datos sobre el impacto del estrés social y ambiental en la salud mental y física para cada país objetivo (Alemania, Francia, Italia, Dinamarca, Irlanda, Luxemburgo, Suiza, Reino Unido, Islandia, Noruega, Suecia, Finlandia, Países Bajos, Bélgica, Austria, Nueva Zelanda, Japón).
- [x] Recopilar datos sobre hostilidad cognitiva, entropía burocrática, paisaje sensorial latente y código social implícito para cada país.
- [x] Recopilar datos sobre precios de vivienda (compra y alquiler) y costo de vida general.
- [x] Investigar políticas y facilidad de integración para inmigrantes.
- [x] Comparar los sistemas de seguridad social de cada país con el de España (eficiencia, gratuidad, copago, atención plena).
- [x] Recopilar datos sobre crimen total, delitos de odio, % voto extrema derecha y tendencia.
- [x] Recopilar datos sobre WJP Rule of Law, protecciones LGTBI+, libertad religiosa y minorías, gasto social/PIB, densidad de servicios sociales.
- [x] Completar datos faltantes de PM10 anual para Reino Unido y otros países restantes.
- [ ] Completar análisis comparativo exhaustivo de todos los sistemas de seguridad social.

### Fase 3: Recopilación de datos detallados por subzona y localidad (Ecosistema Natural, Salud Ambiental y Clima)
- [x] Identificar las subzonas rurales y localidades específicas para cada país según el protocolo.
- [ ] Recopilar datos de PM2.5, PM10, NO2, O3 (valores anuales).
- [ ] Recopilar datos de humedad relativa media y dew point anual.
- [ ] Recopilar datos de polen (índice y taxa dominantes) y mold index.
- [ ] Recopilar datos de radón Bq/m3.
- [ ] Recopilar datos de días de humo/incendio e inversiones térmicas.

### Fase 4: Recopilación de datos detallados por subzona y localidad (Tejido Social, Justicia y Bienestar Humano)
- [ ] Recopilar datos sobre tiempo isócrona a urgencias, hospitales/100k, neumología disponible, camas UCI/100k, telemedicina.
- [ ] Recopilar datos sobre listas de espera para especialistas y cirugías.
- [ ] Recopilar datos sobre ratio de profesionales por habitante (médicos, psicólogos/psiquiatras especializados en TDAH/TLP, pediatras, geriatras, alergólogos e inmunólogos).
- [ ] Recopilar datos sobre coste de copagos y seguros privados.
- [ ] Recopilar datos sobre tasa de suicidios.
- [ ] Investigar programas de salud comunitaria y apoyo a la salud mental accesibles y de calidad.

### Fase 5: Recopilación de datos detallados por subzona y localidad (Estructura Económica y Vivienda)
- [ ] Recopilar datos de €/ha suelo rústico (mediana).
- [ ] Recopilar datos de €/m² compra y alquiler €/mes.
- [ ] Recopilar datos de carga vivienda % renta.
- [ ] Recopilar datos de impuestos y tasas (IBI/Grundsteuer/etc.).
- [ ] Recopilar datos de coste cesta vegana local.
- [ ] Recopilar datos de renta mediana €/mes, paro %, empleo verde/tech %.

### Fase 6: Recopilación de datos detallados por subzona y localidad (Infraestructura, Conectividad y Flujos)
- [ ] Recopilar datos de cobertura fibra %, 5G %.
- [ ] Recopilar datos de latencia ms estimada y fiabilidad eléctrica.
- [ ] Recopilar datos de espacios de cowork rural.

### Fase 7: Recopilación de datos detallados por subzona y localidad (Micro-Sistema y Criterios de Descarte)
- [ ] Recopilar datos de turismo (pernoct/residente), Airbnb/1000 hab, estacionalidad índice.
- [ ] Recopilar datos de ruido dB Lden, luz nocturna (radiancia).
- [ ] Recopilar datos de riesgos: inundación (categoría), sequía (SPEI), incendio (índice), seísmo (PGA), deslizamiento (clase).
- [ ] Recopilar datos de suelo y agua: tipo de suelo (FAO), pH, textura, balance hídrico, derechos/pozos.
- [ ] Recopilar datos de vegano-friendly (tiendas/mercados por 10k), aceptación LGTBI (índice), laicidad (proxy), conflictividad comunitaria.
- [ ] Investigar servicios de asistencia social (comedores, ayuda a domicilio, programas de reinserción y lucha contra adicciones).

### Fase 8: Procesamiento, normalización y cálculo de indicadores
- [ ] Normalizar todas las variables a 0-1 (min-max robusto p5-p95).
- [ ] Calcular los indicadores: Índice Respiratorio (IR), Índice de Progresismo y Seguridad Social (IPSS), Índice de Acceso Sanitario (IAS), Índice de Asequibilidad Rural (IAR), Índice de Sostenibilidad y Bajo Turismo (ISBT), Riesgo Físico-Climático (RFC), Conectividad y Trabajo (ICT), Índice de Aceptación Cultural (IAC).
- [ ] Aplicar la ponderación MCDA (AHP/TOPSIS) para el ranking final.

### Fase 9: Aplicación de filtros duros y análisis de sensibilidad
- [ ] Aplicar los criterios de descarte duros (Hard Filters).
- [ ] Realizar análisis de sensibilidad (tornado y Monte Carlo).

### Fase 10: Generación del informe final y anexos
- [ ] Generar el informe en Word (estructura IMRyD extendida).
- [ ] Crear el paquete de datos (CSV/Excel).
- [ ] Generar gráficos (PNG/SVG): mapas de calor, radares, dispersión, violin/boxplots y cartografía.
- [ ] Incluir apéndices: fuentes, supuestos, imputaciones, control de calidad, replicabilidad.
- [ ] Generar la lista corta (Top 10 global) con justificación clínica-ambiental, coste real de asentamiento, perfil sociopolítico, riesgo climático bajo, conectividad y turismo mínimo.
- [ ] Añadir 3 alternativas backup por continente.

### Fase 11: Entrega de resultados al usuario
- [ ] Enviar el informe final, los datos y los gráficos al usuario.



