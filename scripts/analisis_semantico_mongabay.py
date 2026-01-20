import pandas as pd
import spacy
from collections import Counter
from pathlib import Path

# =========================
# 1. Cargar modelo spaCy
# =========================
nlp = spacy.load("es_core_news_md")

# =========================
# 2. Definir ejes semánticos
# =========================
EJES_SEMANTICOS = {

    "biodiversidad_conservacion": [
        # Ecosistemas
        "biodiversidad", "ecosistema", "bosque", "selva", "amazon",
        "río", "rio", "humedal", "océano", "oceano", "mar",
        "cordillera", "hábitat", "habitat",

        # Especies
        "especie", "fauna", "flora", "animal", "planta",
        "ave", "pez", "mamífero", "mamifero",

        # Conservación
        "conservación", "conservacion", "protección", "proteccion",
        "deforestación", "deforestacion",
        "contaminación", "contaminacion",
        "extinción", "extincion",
        "cambio", "climát", "climat",
        "área", "area", "proteg", "reserva", "parque"
    ],

    "politica_gobernabilidad": [
        "estado", "gobierno", "polít", "polit",
        "autoridad", "ministerio",
        "ley", "decreto", "congreso",
        "justicia", "corte",
        "fiscal", "regul",
        "institu", "sentencia", "derecho"
    ],

    "economia_desarrollo": [
        "econom", "desarroll",
        "invers", "emple",
        "producci", "industr",
        "infraestruct",
        "energ",
        "pesca", "pesquer",
        "agricultur", "agrícol",
        "actividad", "recurso"
    ],

    "sociedad_comunidades": [
        "comunidad", "pueblo",
        "indígen", "indigen",
        "poblac", "sociedad",
        "familia", "territorio",
        "activista",
        "líder", "lider",
        "organiz",
        "impacto", "social"
    ],

    "crimen_ilegalidad": [
        "ilegal", "crimen", "delito", "criminal",
        "asesin", "homicid",
        "violenc",
        "amenaz",
        "tráfic", "trafic",
        "narcotrafic",
        "mafia",
        "grupo", "armado"
    ]
}

# =========================
# 3. Funciones
# =========================
def lematizar(texto):
    doc = nlp(texto.lower())
    return {t.lemma_ for t in doc if t.is_alpha}

def detectar_ejes(titulo):
    lemas = lematizar(titulo)
    ejes = []

    for eje, palabras in EJES_SEMANTICOS.items():
        if any(
            any(lema.startswith(p) for p in palabras)
            for lema in lemas
        ):
            ejes.append(eje)

    return ejes

def activadores_por_eje(titulo):
    lemas = lematizar(titulo)
    resultado = {}

    for eje, palabras in EJES_SEMANTICOS.items():
        activadores = sorted(
            {lema for lema in lemas if any(lema.startswith(p) for p in palabras)}
        )
        if activadores:
            resultado[eje] = activadores

    return resultado

# =========================
# 4. Cargar datos
# =========================
df = pd.read_csv("mongabay_peru_procesado.csv")

# =========================
# 5. Análisis semántico
# =========================
df["ejes_semanticos"] = df["titulo"].apply(detectar_ejes)
df["activadores"] = df["titulo"].apply(activadores_por_eje)
df["sin_eje"] = df["ejes_semanticos"].apply(lambda x: len(x) == 0)

# =========================
# 6. Métricas clave
# =========================
total_titulares = len(df)
titulares_con_eje = len(df[~df["sin_eje"]])
total_asignaciones = sum(len(ejes) for ejes in df["ejes_semanticos"])

print(f"Total de titulares analizados: {total_titulares}")
print(f"Titulares con al menos un eje: {titulares_con_eje}")
print(f"Total de asignaciones semánticas: {total_asignaciones}")

# =========================
# 7. Resumen cuantitativo
# =========================
contador = Counter(
    eje for ejes in df["ejes_semanticos"] for eje in ejes
)

df_resumen = (
    pd.DataFrame(contador.items(), columns=["eje_semantico", "frecuencia"])
    .sort_values("frecuencia", ascending=False)
)

df_resumen.to_csv("resumen_ejes_semanticos.csv", index=False, encoding="utf-8")

# =========================
# 8. Guardar CSV general
# =========================
df.to_csv("mongabay_semantico_con_activadores.csv", index=False, encoding="utf-8")

# =========================
# 9. Guardar desgloses por eje
# =========================
output_dir = Path("desglose_ejes")
output_dir.mkdir(exist_ok=True)

for eje in EJES_SEMANTICOS.keys():
    df_eje = df[df["ejes_semanticos"].apply(lambda x: eje in x)].copy()
    df_eje["activadores_eje"] = df_eje["activadores"].apply(
        lambda d: ", ".join(d.get(eje, []))
    )
    df_eje.to_csv(output_dir / f"{eje}.csv", index=False, encoding="utf-8")

print("Desglose por ejes semánticos completado.")




