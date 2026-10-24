SYNTHETIC TEST DOCUMENT — fictional study written for evaluating the stress-rep-guideline skill; not real research

# Dinámica de la transmisión del dengue en Villa Ficticia: un modelo de dinámica de sistemas

C. Ficticio y D. Inventada — Instituto Imaginario de Salud Pública (institución ficticia)

## 1. Propósito del modelo

Villa Ficticia (ciudad ficticia de 420.000 habitantes) registró en 2023 dos brotes de dengue con un pico de 310 casos semanales. La Secretaría de Salud solicitó un modelo que permitiera comparar dos políticas de control —fumigación focalizada y una campaña de eliminación de criaderos— en cuanto a su efecto sobre la incidencia y las hospitalizaciones durante dos años. Construimos un modelo de dinámica de sistemas (DS) de tipo compartimental para responder a esa pregunta. El modelo está pensado como herramienta de apoyo a la planificación local; no pretende predecir con exactitud el número de casos.

## 2. Variables de salida

Se reportan tres variables de salida en todos los experimentos:

- Incidencia semanal de casos sintomáticos (casos/semana), igual al flujo de infección multiplicado por la fracción sintomática, registrado en cada paso de tiempo y agregado por semana.
- Prevalencia de infectados (personas), igual al valor del acervo *Infectados* al final de cada semana.
- Hospitalizaciones acumuladas (personas), igual al acervo *Hospitalizados acumulados* al final de la simulación.

## 3. Objetivos de la experimentación

El modelo se utilizó para el análisis de dos políticas y para su comparación con el caso base:

| Política | Descripción | Justificación |
|---|---|---|
| P0 | Caso base: sin intervención adicional | Situación actual |
| P1 | Fumigación focalizada: reduce la tasa de contacto efectivo en un 30 % durante 8 semanas a partir de la semana 20 | Intervención habitual de la Secretaría |
| P2 | Campaña de eliminación de criaderos: reduce la tasa de contacto efectivo en un 15 % de forma permanente a partir de la semana 10 | Propuesta de la mesa comunitaria |

Además se realizó un análisis de sensibilidad univariado variando cuatro parámetros (tasa de contacto, periodo de incubación, periodo infeccioso y fracción hospitalizada) en ±20 % respecto del caso base, de uno en uno. No se utilizó optimización por simulación.

## 4. Lógica del modelo

### 4.1 Diagrama general del modelo base

La Figura 1 es el diagrama causal del modelo y la Figura 2 el diagrama de acervos y flujos. Los bucles de retroalimentación clave son: B1 (agotamiento de susceptibles: más infectados → menos susceptibles → menos infecciones nuevas), R1 (contagio: más infectados → más contactos infecciosos → más infecciones nuevas) y B2 (recuperación: más infectados → más recuperaciones → menos infectados). Los diagramas completos con todas las variables auxiliares se incluyen en la Figura S1 del material suplementario.

### 4.2 Lógica del modelo base

El comportamiento del modelo está gobernado por la interacción del bucle de refuerzo R1 con el bucle de balance B1: al inicio del brote domina R1 y la incidencia crece de forma aproximadamente exponencial; a medida que el acervo de susceptibles se agota, B1 domina y la incidencia cae. El bucle B2 fija la duración media del periodo infeccioso. El multiplicador estacional de contacto (sección 4.5) desplaza el equilibrio entre R1 y B1 a lo largo del año, lo que produce los dos picos anuales observados. No se utilizan arquetipos de sistemas.

### 4.3 Lógica de escenarios

Las políticas P1 y P2 no modifican la estructura del modelo: actúan únicamente sobre la variable auxiliar *factor de intervención*, que multiplica la tasa de contacto efectivo (igual a 1 en el caso base, 0,70 entre las semanas 20 y 28 en P1, y 0,85 a partir de la semana 10 en P2). El análisis de sensibilidad modifica los valores de los parámetros indicados en la sección 3 sin cambiar las ecuaciones.

### 4.4 Algoritmos

El modelo no contiene algoritmos que imiten procesos manuales o complejos del mundo real: todas las relaciones son ecuaciones algebraicas o diferenciales explícitas listadas en la sección 4.5.

### 4.5 Componentes

**Acervos (niveles).** Todos en unidades de personas: *Susceptibles* (S), *Expuestos* (E), *Infectados* (I), *Recuperados* (R) y *Hospitalizados acumulados* (H). La Tabla 1 indica para cada acervo sus flujos de entrada y de salida.

| Acervo | Entradas | Salidas | Papel en el modelo |
|---|---|---|---|
| Susceptibles | — | infección | población en riesgo |
| Expuestos | infección | inicio de síntomas | retraso de incubación |
| Infectados | inicio de síntomas | recuperación | fuente de contagio |
| Recuperados | recuperación | — | inmunes (sumidero de la epidemia) |
| Hospitalizados acumulados | hospitalización | — | contador de resultados |

**Flujos (tasas).** Todos en personas/semana:

- infección = β · m(t) · f · S · I / N, donde β es la tasa de contacto efectivo, m(t) el multiplicador estacional y f el factor de intervención;
- inicio de síntomas = E / τ_E (retraso de primer orden con tiempo medio τ_E);
- recuperación = I / τ_I (retraso de primer orden con tiempo medio τ_I);
- hospitalización = h · inicio de síntomas (flujo paralelo que alimenta el contador H sin extraer personas de I).

**Constantes y variables auxiliares.**

| Variable | Ecuación o valor | Unidad |
|---|---|---|
| N | S + E + I + R | personas |
| β (tasa de contacto efectivo) | 1,85 | 1/semana |
| τ_E (periodo de incubación) | 0,9 | semanas |
| τ_I (periodo infeccioso) | 1,1 | semanas |
| h (fracción hospitalizada) | 0,06 | adimensional |
| factor de intervención f | 1 (P0); según sección 4.3 (P1, P2) | adimensional |
| multiplicador estacional m(t) | tabla de búsqueda (abajo) | adimensional |

**Funciones gráficas / tablas de búsqueda.** El multiplicador estacional de contacto m(t) es una tabla de 12 valores mensuales (enero 0,8; febrero 0,9; marzo 1,1; abril 1,3; mayo 1,4; junio 1,2; julio 1,0; agosto 0,9; septiembre 1,0; octubre 1,1; noviembre 1,2; diciembre 1,0) interpolada linealmente; se construyó a partir del índice de infestación mensual publicado por la Secretaría de Salud de Villa Ficticia.

**Fuentes y sumideros.** El modelo no incluye nacimientos ni muertes (población cerrada), por lo que no hay fuentes infinitas; el único sumidero es el acervo *Recuperados*, que no tiene salida.

## 5. Datos

### 5.1 Fuentes de datos

Los parámetros epidemiológicos (β, τ_E, τ_I, h) provienen de la literatura (Ficticio et al., 2021; Inventada, 2019). Los datos de casos semanales provienen del boletín epidemiológico semanal de la Secretaría de Salud de Villa Ficticia, y el índice de infestación mensual de la misma fuente.

### 5.2 Preprocesamiento

Las series de casos semanales se suavizaron con una media móvil de tres semanas antes de la comparación con el modelo. Dos semanas sin reporte (semanas 31 y 32 de 2023) se completaron por interpolación lineal entre las semanas adyacentes.

### 5.3 Parámetros de entrada

Los valores del caso base figuran en la tabla de la sección 4.5. En el análisis de sensibilidad, β varía entre 1,48 y 2,22; τ_E entre 0,72 y 1,08; τ_I entre 0,88 y 1,32; y h entre 0,048 y 0,072. Las políticas P1 y P2 solo cambian el factor de intervención (sección 4.3). El modelo no utiliza entradas estocásticas, por lo que no se emplean distribuciones de probabilidad.

### 5.4 Supuestos

Donde no había datos se asumió: (i) población cerrada sin nacimientos, muertes ni migración durante los dos años simulados, porque el periodo es corto respecto de la dinámica demográfica; (ii) mezcla homogénea de la población, porque no se dispone de datos de contacto por barrio; (iii) inmunidad permanente tras la recuperación, porque el modelo representa un único serotipo; (iv) el multiplicador estacional del año 2023 se repite en 2024 y 2025.

## 6. Experimentación

### 6.1 Inicialización

Valores iniciales de los acervos en la semana 0 (1 de enero de 2024): S = 395.000; E = 60; I = 40; R = 24.900; H = 0 (personas). Las variables auxiliares se inicializan con los valores de la tabla de la sección 4.5 (f = 1; m(0) = 0,8). Los valores iniciales no se varían entre corridas.

### 6.2 Duración de la simulación

Cada corrida cubre 104 semanas; la unidad de tiempo es la semana.

### 6.3 Enfoque de estimación

El modelo es totalmente determinista; no se utilizan entradas estocásticas y cada política se evalúa con una única corrida. El modelo se calibró frente a los casos semanales reportados de 2023.

## 7. Implementación

### 7.1 Software

El modelo se implementó en Vensim PLE 9.3.4 sobre Windows 11 Pro versión 23H2 (compilación 22631). No se utilizan acervos especializados (transportadores, colas ni hornos). No se utilizó ningún lenguaje de programación de propósito general ni paquetes adicionales.

### 7.2 Ejecución del modelo

Método de integración: Euler, con paso de tiempo DT = 0,25 semanas. Se verificó que al reducir DT a 0,125 los resultados cambian menos del 0,5 %.

## 8. Acceso al modelo

El archivo del modelo (.mdl), la tabla de búsqueda estacional y las series de casos utilizadas se incluyen como material suplementario de este artículo.

## 9. Resultados (resumen)

En el caso base el modelo reproduce los dos picos de 2023 con un error absoluto medio de 22 casos/semana. P2 reduce las hospitalizaciones acumuladas a dos años en un 27 % frente a un 9 % para P1.
