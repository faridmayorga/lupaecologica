# 🔍 Lupa Ecológica
### Mapeo Semántico de la Agenda Ambiental en el Perú (2020–2025)

---

## 1. Marco Institucional: ¿Qué es Mongabay?
**Mongabay** es una organización mediática independiente y sin fines de lucro que informa sobre la naturaleza y los desafíos planetarios a través de una red global de periodistas locales. Su labor se centra en:

* **Transparencia y Rendición de Cuentas:** Revelar evidencia de la destrucción de ecosistemas y sus consecuencias para las personas, creando oportunidades para que los responsables rindan cuentas.
* **Accesibilidad de la Ciencia:** Cerrar brechas de conocimiento traduciendo la información científica en formatos accesibles y gratuitos en múltiples idiomas.
* **Amplificación de Voces:** Elevar el conocimiento de las poblaciones directamente impactadas por el cambio ambiental, abordando la salud de los sistemas de la Tierra desde una perspectiva de derechos y evidencia.

---

## 2. Objetivo de la Investigación
Esta investigación es de carácter **exploratorio** y busca identificar las prioridades temáticas y los patrones discursivos en la cobertura periodística sobre el Perú durante la primera mitad de la década actual (2020-2025).

El objetivo principal es determinar cómo se distribuye el interés informativo entre distintos ejes de crisis y conservación, permitiendo visualizar qué aspectos del deterioro ambiental o de la gestión de recursos reciben mayor atención mediática en un país megadiverso y vulnerable.

---

## 3. Metodología Técnica
El proceso se divide en una fase de recolección automatizada y una fase de procesamiento lingüístico:

### Extracción de Datos
Se desarrolló un script en **Python** utilizando las librerías `Requests` y `BeautifulSoup` para realizar el raspado (*scraping*) de 41 páginas del archivo histórico de Mongabay Perú.
* **Campos recolectados:** Titular, autor, fecha de publicación y enlace directo.

### Procesamiento con spaCy y "Activadores"
Para el análisis de los textos, se empleó **spaCy**, una biblioteca de procesamiento de lenguaje natural (NLP) de nivel industrial.
* **Lematización:** El modelo `es_core_news_md` reduce cada palabra a su raíz lingüística (**lema**), permitiendo identificar conceptos independientemente de sus conjugaciones o plurales.
* **Detección por Activadores:** El sistema utiliza términos específicos asociados a cada eje semántico.
* **Transparencia de datos:** Los activadores exactos que categorizaron cada noticia se detallan fila por fila en los archivos CSV finales para permitir la verificación manual.

---

## 4. Descripción del Corpus (2020–2025)
* **Rango Temporal:** Del 1 de enero de 2020 al 31 de diciembre de 2025.
* **Volumen de Datos:** 1,201 titulares analizados.
* **Geografía:** Contenido etiquetado específicamente para el contexto peruano.

---

## 5. Limitaciones del Estudio
* **Unidad de Análisis:** Se limita exclusivamente a los titulares. No procesa el cuerpo de los artículos ni multimedia.
* **Nivel Semántico:** La detección se basa en coincidencia léxica mediante lemas; no realiza análisis de sentimiento profundo.
* **Definición de Ejes:** Las categorías son predefinidas por el investigador (enfoque deductivo).

---

## 6. Resultados Cuantitativos
| Eje Semántico | Frecuencia (Menciones) |
| :--- | :---: |
| **Biodiversidad y Conservación** | 584 |
| **Política y Gobernabilidad** | 281 |
| **Sociedad y Comunidades** | 237 |
| **Economía y Desarrollo** | 230 |
| **Crimen e Ilegalidad** | 148 |

* **Titulares con al menos un eje identificado:** 978.
* **Total de asignaciones semánticas:** 1,480 (noticias multidimensionales).

---

## 7. Conclusiones Descriptivas
1.  **Frecuencia Temática:** Prevalencia marcada del eje "Biodiversidad y Conservación".
2.  **Multitematicidad:** La cobertura tiende a relacionar problemas ambientales con múltiples dimensiones (ej. política y sociedad) simultáneamente.
3.  **Identificación Exitosa:** El modelo categorizó el **81.4%** de la muestra total, reflejando consistencia en el lenguaje de la fuente.
4.  **Potencial de Investigación:** Base para futuros estudios sobre tendencias temporales, análisis de cuerpos de texto completos o comparaciones regionales.
