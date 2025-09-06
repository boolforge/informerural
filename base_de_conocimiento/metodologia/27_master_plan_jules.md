# Plan de Trabajo Maestro v2 (Jules)

**Propietario:** Agente Jules
**Fecha de Inicio:** 2025-09-06
**Basado en:** `25_plan_de_trabajo_y_progreso.md` y auditoría forense `audits/manus_forensic_review.md`.

---

## Misión General
Continuar y completar el proyecto `informerural`, corrigiendo los fallos de proceso del agente anterior y aplicando un nivel superior de rigor, documentación y proactividad.

---

## Fases y Tareas

### **PARTE A: Remediación y Mejora de Protocolos (Trabajo de Jules)**

#### **Fase 12: Implementación de Protocolos v7.0**
*   [ ] **Tarea 12.1:** Implementar `AGENT.md` v7.0, que debe incluir:
    *   [ ] Un nuevo "Protocolo de Arranque y Calibración (PAC)".
    *   [ ] Refuerzo de la directiva del Protocolo de Registro de Actividad (PRA).
    *   [ ] Introducción del sistema `checkpoint.json` para la persistencia del estado.
*   [ ] **Tarea 12.2:** Diseñar y documentar el script conceptual `update_checkpoint.py`.
*   [ ] **Tarea 12.3:** Crear el archivo `checkpoint.json` inicial.

### **PARTE B: Tareas de Investigación Pendientes (Heredadas de Manus)**

#### **Fase 3: Recopilación de datos detallados por subzona y localidad (Ecosistema Natural, Salud Ambiental y Clima)**
*   [ ] **Tarea 3.1:** Recopilar datos de PM2.5, PM10, NO2, O3 (valores anuales).
*   [ ] **Tarea 3.2:** Recopilar datos de humedad relativa media y dew point anual.
*   [ ] **Tarea 3.3:** Recopilar datos de polen (índice y taxa dominantes) y mold index.
*   [ ] **Tarea 3.4:** Recopilar datos de radón Bq/m3.
*   [ ] **Tarea 3.5:** Recopilar datos de días de humo/incendio e inversiones térmicas.

#### **Fase 4: Recopilación de datos detallados por subzona y localidad (Tejido Social, Justicia y Bienestar Humano)**
*   [ ] **Tarea 4.1:** Recopilar datos sobre tiempo isócrona a urgencias, hospitales/100k, neumología disponible, camas UCI/100k, telemedicina.
*   [ ] **Tarea 4.2:** Recopilar datos sobre listas de espera para especialistas y cirugías.
*   [ ] **Tarea 4.3:** Recopilar datos sobre ratio de profesionales por habitante (médicos, psicólogos/psiquiatras especializados, etc.).
*   [ ] **Tarea 4.4:** Recopilar datos sobre coste de copagos y seguros privados.
*   [ ] **Tarea 4.5:** Recopilar datos sobre tasa de suicidios.
*   [ ] **Tarea 4.6:** Investigar programas de salud comunitaria y apoyo a la salud mental.
*   [ ] **Tarea 4.7 (Heredada):** Completar análisis comparativo exhaustivo de todos los sistemas de seguridad social con España.

#### **Fase 5: Recopilación de datos detallados por subzona y localidad (Estructura Económica y Vivienda)**
*   [ ] **Tarea 5.1:** Recopilar datos de €/ha suelo rústico (mediana).
*   [ ] **Tarea 5.2:** Recopilar datos de €/m² compra y alquiler €/mes.
*   [ ] **Tarea 5.3:** Recopilar datos de carga vivienda % renta.
*   [ ] **Tarea 5.4:** Recopilar datos de impuestos y tasas (IBI/Grundsteuer/etc.).
*   [ ] **Tarea 5.5:** Recopilar datos de coste cesta vegana local.
*   [ ] **Tarea 5.6:** Recopilar datos de renta mediana €/mes, paro %, empleo verde/tech %.

#### **Fase 6: Recopilación de datos detallados por subzona y localidad (Infraestructura, Conectividad y Flujos)**
*   [ ] **Tarea 6.1:** Recopilar datos de cobertura fibra %, 5G %.
*   [ ] **Tarea 6.2:** Recopilar datos de latencia ms estimada y fiabilidad eléctrica.
*   [ ] **Tarea 6.3:** Recopilar datos de espacios de cowork rural.

#### **Fase 7: Recopilación de datos detallados por subzona y localidad (Micro-Sistema y Criterios de Descarte)**
*   [ ] **Tarea 7.1:** Recopilar datos de turismo (pernoct/residente), Airbnb/1000 hab, estacionalidad índice.
*   [ ] **Tarea 7.2:** Recopilar datos de ruido dB Lden, luz nocturna (radiancia).
*   [ ] **Tarea 7.3:** Recopilar datos de riesgos: inundación, sequía, incendio, seísmo, deslizamiento.
*   [ ] **Tarea 7.4:** Recopilar datos de suelo y agua: tipo de suelo, pH, textura, etc.
*   [ ] **Tarea 7.5:** Recopilar datos de vegano-friendly, aceptación LGTBI, etc.
*   [ ] **Tarea 7.6:** Investigar servicios de asistencia social.

### **PARTE C: Ejecución del Análisis y Entrega Final (Trabajo de Jules)**

#### **Fase 8: Procesamiento, normalización y cálculo de indicadores**
*   [ ] **Tarea 8.1:** Normalizar todas las variables a 0-1 (min-max robusto p5-p95).
*   [ ] **Tarea 8.2:** Calcular los 8 indicadores compuestos.
*   [ ] **Tarea 8.3:** Aplicar la ponderación MCDA (AHP/TOPSIS) para el ranking final.

#### **Fase 9: Aplicación de filtros duros y análisis de sensibilidad**
*   [ ] **Tarea 9.1:** Aplicar los criterios de descarte duros.
*   [ ] **Tarea 9.2:** Realizar análisis de sensibilidad.

#### **Fase 10: Generación del informe final y anexos**
*   [ ] **Tarea 10.1:** Generar el informe en Word (estructura IMRyD extendida).
*   [ ] **Tarea 10.2:** Crear el paquete de datos (CSV/Excel).
*   [ ] **Tarea 10.3:** Generar todos los gráficos requeridos.
*   [ ] **Tarea 10.4:** Incluir todos los apéndices.
*   [ ] **Tarea 10.5:** Generar la lista corta (Top 10 global) con narrativas detalladas.

#### **Fase 11: Entrega de resultados al usuario**
*   [ ] **Tarea 11.1:** Enviar el informe final, los datos y los gráficos al usuario.
