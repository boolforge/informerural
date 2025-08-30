## Tareas Pendientes - Macroanálisis y Macrorreporte

### Fase 1: Análisis y Comprensión del Protocolo de Investigación (Completada)
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
- [x] Procesar completamente `paramanus.txt` y extraer toda la información relevante, organizándola para su uso futuro.

### Fase 2: Recopilación de Datos Macro-Contextuales y Socio-Políticos por País (En Progreso)
- [x] Investigar y recopilar datos sobre el impacto del estrés social y ambiental en la salud mental y física para cada país objetivo (Alemania, Francia, Italia, Dinamarca, Irlanda, Luxemburgo, Suiza, Reino Unido, Islandia, Noruega, Suecia, Finlandia, Países Bajos, Bélgica, Austria, Nueva Zelanda, Japón).
- [x] Recopilar datos sobre hostilidad cognitiva, entropía burocrática, paisaje sensorial latente y código social implícito para cada país.
- [x] Recopilar datos sobre precios de vivienda (compra y alquiler) y costo de vida general.
- [x] Investigar políticas y facilidad de integración para inmigrantes.
- [ ] Comparar los sistemas de seguridad social de cada país con el de España (eficiencia, gratuidad, copago, atención plena). (Pendiente: Requiere análisis comparativo exhaustivo).
- [x] Recopilar datos sobre crimen total, delitos de odio, % voto extrema derecha y tendencia.
- [x] Recopilar datos sobre WJP Rule of Law, protecciones LGTBI+, libertad religiosa y minorías, gasto social/PIB, densidad de servicios sociales.
- [x] Completar datos faltantes de PM10 anual para Reino Unido y otros países restantes.

### Fase 3: Recopilación de Datos Detallados por Subzona y Localidad (Ecosistema Natural, Salud Ambiental y Clima) (En Progreso)
- [x] Identificar las subzonas rurales y localidades específicas para cada país según el protocolo.
  - [ ] Recopilar datos de PM2.5, PM10, NO2, O3 (valores anuales). (En progreso: La descarga de la EEA ha fallado. Se está investigando la API de Copernicus para obtener estos datos. Se ha intentado con el dataset cams-global-atmospheric-composition-forecasts y cams-europe-air-quality-reanalyses con tipo \'reanalysis\' y ha fallado. Se investigará la documentación de Copernicus para encontrar la combinación correcta de parámetros. Paralelamente, se inició la recopilación de datos de seguridad social).
  - [ ] Recopilar datos de seguridad social para los países desarrollados. (En progreso: Se han identificado fuentes iniciales como OECD, Eurostat, SSA).
- [ ] Recopilar datos de humedad relativa media y dew point anual.
- [ ] Recopilar datos de polen (índice y taxa dominantes) y mold index.
- [ ] Recopilar datos de radón Bq/m3.
- [ ] Recopilar datos de días de humo/incendio e inversiones térmicas.

### Fase 4: Recopilación de Datos Detallados por Subzona y Localidad (Tejido Social, Justicia y Bienestar Humano) (Pendiente)
- [ ] Recopilar datos sobre tiempo isócrona a urgencias, hospitales/100k, neumología disponible, camas UCI/100k, telemedicina.
- [ ] Recopilar datos sobre listas de espera para especialistas y cirugías.
- [ ] Recopilar datos sobre ratio de profesionales por habitante (médicos, psicólogos/psiquiatras especializados en TDAH/TLP, pediatras, geriatras, alergólogos e inmunólogos).
- [ ] Recopilar datos sobre coste de copagos y seguros privados.
- [ ] Recopilar datos sobre tasa de suicidios.
- [ ] Investigar programas de salud comunitaria y apoyo a la salud mental accesibles y de calidad.

### Fase 5: Recopilación de Datos Detallados por Subzona y Localidad (Estructura Económica y Vivienda) (Pendiente)
- [ ] Recopilar datos de €/ha suelo rústico (mediana).
- [ ] Recopilar datos de €/m² compra y alquiler €/mes.
- [ ] Recopilar datos de carga vivienda % renta.
- [ ] Recopilar datos de impuestos y tasas (IBI/Grundsteuer/etc.).
- [ ] Recopilar datos de coste cesta vegana local.
- [ ] Recopilar datos de renta mediana €/mes, paro %, empleo verde/tech %.

### Fase 6: Recopilación de Datos Detallados por Subzona y Localidad (Infraestructura, Conectividad y Flujos) (Pendiente)
- [ ] Recopilar datos de cobertura fibra %, 5G %.
- [ ] Recopilar datos de latencia ms estimada y fiabilidad eléctrica.
- [ ] Recopilar datos de espacios de cowork rural.

### Fase 7: Recopilación de Datos Detallados por Subzona y Localidad (Micro-Sistema y Criterios de Descarte) (Pendiente)
- [ ] Recopilar datos de turismo (pernoct/residente), Airbnb/1000 hab, estacionalidad índice.
- [ ] Recopilar datos de ruido dB Lden, luz nocturna (radiancia).
- [ ] Recopilar datos de riesgos: inundación (categoría), sequía (SPEI), incendio (índice), seísmo (PGA), deslizamiento (clase).
- [ ] Recopilar datos de suelo y agua: tipo de suelo (FAO), pH, textura, balance hídrico, derechos/pozos.
- [ ] Recopilar datos de vegano-friendly (tiendas/mercados por 10k), aceptación LGTBI (índice), laicidad (proxy), conflictividad comunitaria.
- [ ] Investigar servicios de asistencia social (comedores, ayuda a domicilio, programas de reinserción y lucha contra adicciones).

### Fase 8: Procesamiento, Normalización y Cálculo de Indicadores (Pendiente)
- [ ] Normalizar todas las variables a 0-1 (min-max robusto p5-p95).
- [ ] Calcular los indicadores: Índice Respiratorio (IR), Índice de Progresismo y Seguridad Social (IPSS), Índice de Acceso Sanitario (IAS), Índice de Asequibilidad Rural (IAR), Índice de Sostenibilidad y Bajo Turismo (ISBT), Riesgo Físico-Climático (RFC), Conectividad y Trabajo (ICT), Índice de Aceptación Cultural (IAC).
- [ ] Aplicar la ponderación MCDA (AHP/TOPSIS) para el ranking final.

### Fase 9: Aplicación de Filtros Duros y Análisis de Sensibilidad (Pendiente)
- [ ] Aplicar los criterios de descarte duros (Hard Filters).
- [ ] Realizar análisis de sensibilidad (tornado y Monte Carlo).

### Fase 10: Generación del Informe Final y Anexos (Pendiente)
- [ ] Generar el informe en Word (estructura IMRyD extendida).
- [ ] Crear el paquete de datos (CSV/Excel).
- [ ] Generar gráficos (PNG/SVG): mapas de calor, radares, dispersión, violin/boxplots y cartografía.
- [ ] Incluir apéndices: fuentes, supuestos, imputaciones, control de calidad, replicabilidad.
- [ ] Generar la lista corta (Top 10 global) con justificación clínica-ambiental, coste real de asentamiento, perfil sociopolítico, riesgo climático bajo, conectividad y turismo mínimo.
- [ ] Añadir 3 alternativas backup por continente.

### Fase 11: Entrega de Resultados al Usuario (Pendiente)
- [ ] Enviar el informe final, los datos y los gráficos al usuario.


## Estrategia de Gestión del Contexto y Eficiencia:

Para superar las limitaciones de contexto y mejorar la eficiencia, implementaré las siguientes estrategias:

1.  **Documentación Exhaustiva y Centralizada (KB y `todo.md`):**
    *   Todas las decisiones, hallazgos, fuentes de datos, scripts, errores y soluciones se registrarán de forma detallada en la KB (`kb_index.md`) y en el `todo.md`.
    *   El `kb_index.md` actuará como un índice maestro, con enlaces a documentos más detallados cuando sea necesario.
    *   Cada vez que se complete o se avance en una tarea, se actualizará el `todo.md` de forma inmediata y explícita.
    *   Se incluirán secciones de "Lecciones Aprendidas" y "Próximos Pasos Estratégicos" en la KB para cada fase completada o en progreso.

2.  **Iteración y Verificación Constante:**
    *   Antes de iniciar una nueva acción, se realizará una revisión rápida del `todo.md` y la KB para asegurar que no se dupliquen esfuerzos y que se siga la estrategia planificada.
    *   Cada resultado de una acción será verificado y validado antes de proceder al siguiente paso.
    *   Se priorizará la automatización de tareas repetitivas para maximizar la eficiencia.

3.  **Gestión de Errores y Alternativas:**
    *   Cuando surja un error o un bloqueo (como con la API de Irlanda), se documentará el problema, las causas identificadas y las soluciones intentadas en la KB.
    *   Se buscarán activamente fuentes de datos o metodologías alternativas si la vía principal presenta obstáculos significativos, documentando siempre el porqué del cambio.

4.  **Comunicación Explícita:**
    *   Mis mensajes al usuario serán más detallados, explicando no solo lo que estoy haciendo, sino *por qué* lo estoy haciendo y *cómo* se alinea con el plan general y el `todo.md`.
    *   Se proporcionarán actualizaciones regulares sobre el progreso y los desafíos.

5.  **Deduplicación Inteligente de Información:**
    *   Al integrar nueva información o al revisar documentos existentes, se aplicará un proceso de deduplicación y consolidación inteligente, eliminando redundancias y sintetizando la información de manera concisa y útil.
    *   Se utilizarán referencias cruzadas en la KB para evitar la repetición de contenido.

**Próximos Pasos Inmediatos:**

1.  **Recopilación de datos de seguridad social:** Continuar con la recopilación de datos de seguridad social para los países desarrollados, utilizando las fuentes identificadas (OECD, Eurostat, SSA).
2.  **Resolución de problemas de la API de Copernicus:** Continuar investigando la documentación de Copernicus para encontrar la combinación correcta de parámetros para la descarga de datos de calidad del aire.
3.  **Documentar en la KB:** Registrar los avances, desafíos y lecciones aprendidas en la KB para asegurar la herencia de contexto.


- [ ] Recopilar datos de polen (índice y taxa dominantes) y mold index.
  - [ ] Fuentes identificadas: Copernicus, European Pollen Database (EPD), Polleninformation.at, AccuWeather, EAN.


- [ ] Recopilar datos de radón Bq/m3.
  - [ ] Fuentes identificadas: European Indoor Radon Map (JRC), WHO, traceRadon, Airthings.


- [ ] Recopilar datos de humedad relativa media y dew point anual.
  - [ ] Fuentes identificadas: Copernicus Climate Change Service (C3S), Global Data Lab, ECAD, Open-Meteo.com, NOAA ISD.


- [x] Recopilar datos de seguridad social para los países desarrollados. (En progreso: Se ha intentado descargar datos de Eurostat, pero la descarga directa a la sandbox no es posible. Se buscará una alternativa o se intentará obtener los datos a través de una API si está disponible.)


- [ ] Recopilar datos de seguridad social para los países desarrollados. (En progreso: La descarga de Eurostat vía API ha fallado con parámetros específicos. Se investigarán los parámetros correctos para el dataset tps00101.)

