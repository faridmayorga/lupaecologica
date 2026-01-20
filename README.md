# lupaecologica
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

* **Campos recolectados:** De cada artículo se extrajo el titular, el autor, la fecha de publicación y el enlace directo.

### Procesamiento con spaCy y "Activadores"
Para el análisis de los textos, se empleó **spaCy**, una biblioteca de procesamiento de lenguaje natural (NLP) de nivel industrial.

* **Lematización:** El modelo `es_core_news_md` analiza cada palabra del titular y la reduce a su raíz lingüística (**lema**), permitiendo identificar conceptos independientemente de sus conjugaciones o plurales.
* **Detección por Activadores:** El sistema utiliza **"activadores"**, que son términos específicos asociados a cada eje semántico.
* **Transparencia de datos:** Una noticia puede estar vinculada a uno o varios campos temáticos simultáneamente. Los activadores exactos que activaron cada categoría se encuentran detallados fila por fila en los archivos CSV finales para permitir la verificación manual.

---

## 4. Descripción del Corpus (2020–2025)
El análisis se concentra en un periodo crítico de transformaciones globales y locales:

* **Rango Temporal:** Del 1 de enero de 2020 al 31 de diciembre de 2025.
* **Volumen de Datos:** 1,201 titulares analizados.
* **Geografía:** Contenido etiquetado y filtrado específicamente para el contexto peruano.

---

## 5. Limitaciones del Estudio
* **Unidad de Análisis:** El estudio se limita exclusivamente a los **titulares** de las noticias. No procesa el cuerpo de los artículos, los pies de foto ni el contenido multimedia.
* **Nivel de Análisis Semántico:** La detección de ejes se basa en una técnica de **coincidencia léxica mediante lemas**. El algoritmo identifica la presencia de conceptos clave, pero no realiza un análisis de sentimiento profundo ni interpreta ironías.
* **Definición de Ejes:** Las categorías (ejes semánticos) fueron predefinidas por el investigador, lo que implica un enfoque deductivo sobre la muestra de datos.

---

## 6. Resultados Cuantitativos
El procesamiento de los titulares mediante los diccionarios de lemas arrojó los siguientes datos:

* **Titulares con al menos un eje identificado:** 978.
* **Total de asignaciones semánticas:** 1,480 (indicando que un alto porcentaje de noticias tocan más de un tema).

### Distribución por Frecuencia
| Eje Semántico | Frecuencia (Menciones) |
| :--- | :---: |
| Biodiversidad y Conservación | 650 |
| Sociedad y Comunidades | 289 |
| Crimen e Ilegalidad | 285 |
| Economía y Desarrollo | 145 |
| Política y Gobernabilidad | 111 |

---

## 7. Conclusiones Descriptivas
* **Frecuencia Temática:** Se observa una prevalencia marcada del eje **"Biodiversidad y Conservación"**, que acumula la mayor cantidad de activadores detectados en el periodo 2020-2025.
* **Multitematicidad:** La diferencia entre el número de titulares clasificados (978) y el total de asignaciones (1,480) confirma que la cobertura de Mongabay sobre el Perú tiende a relacionar los problemas ambientales con múltiples dimensiones (ej. política y sociedad) en un mismo titular.
* **Identificación Exitosa:** El modelo logró categorizar el **81.4%** de la muestra total, lo que indica que el lenguaje utilizado en los titulares de Mongabay es altamente consistente con los ejes semánticos definidos.
* **Potencial de Investigación:** Este análisis sienta las bases para futuras investigaciones que podrían incluir el procesamiento del cuerpo completo de las noticias, el análisis de tendencias temporales por año o la comparación de agendas entre diferentes países de la región.
