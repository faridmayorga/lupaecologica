import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from datetime import datetime

# -----------------------------
# CONFIGURACIÓN
# -----------------------------
ruta_carpeta = os.path.expanduser("~/Desktop/mongabay")
os.makedirs(ruta_carpeta, exist_ok=True)

base_url = "https://es.mongabay.com/list/peru/"
headers = {"User-Agent": "Mozilla/5.0"}

meses = {
    "Ene": "01", "Feb": "02", "Mar": "03", "Abr": "04",
    "May": "05", "Jun": "06", "Jul": "07", "Ago": "08",
    "Sep": "09", "Oct": "10", "Nov": "11", "Dic": "12"
}

def parse_fecha(fecha_str):
    try:
        partes = fecha_str.split()
        dia = partes[0]
        mes = meses.get(partes[1])
        anio = partes[2]
        fecha_iso = f"{anio}-{mes}-{dia.zfill(2)}"
        return datetime.strptime(fecha_iso, "%Y-%m-%d")
    except:
        return None

raw_data = []

# -----------------------------
# SCRAPING
# -----------------------------
for page in range(1, 42):
    url = base_url if page == 1 else f"{base_url}page/{page}"
    print(f"Scrapeando página {page}")

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    articulos = soup.find_all("div", class_="article--container")

    for art in articulos:
        titulo = art.find("h3").get_text(strip=True) if art.find("h3") else None

        a = art.find("a", href=True)
        link = a["href"] if a else None

        fecha_span = art.find("span", class_="date")
        fecha = fecha_span.get_text(strip=True) if fecha_span else None

        autor_span = art.find("span", class_="byline")
        autor = autor_span.get_text(strip=True) if autor_span else None

        if titulo and link and fecha:
            raw_data.append({
                "titulo": titulo,
                "fecha": fecha,
                "autor": autor,
                "link": link
            })

# -----------------------------
# CSV NO PROCESADO
# -----------------------------
df_raw = pd.DataFrame(raw_data)
ruta_raw = os.path.join(ruta_carpeta, "mongabay_peru_raw.csv")
df_raw.to_csv(ruta_raw, index=False, encoding="utf-8")

# -----------------------------
# CSV PROCESADO
# -----------------------------
df_proc = df_raw.copy()

df_proc["fecha_dt"] = df_proc["fecha"].apply(parse_fecha)
df_proc = df_proc.dropna(subset=["fecha_dt"])

# Filtro temporal: 2020–2025
fecha_inicio = datetime(2020, 1, 1)
fecha_fin = datetime(2025, 12, 31)

df_proc = df_proc[
    (df_proc["fecha_dt"] >= fecha_inicio) &
    (df_proc["fecha_dt"] <= fecha_fin)
]

df_proc["fecha_iso"] = df_proc["fecha_dt"].dt.strftime("%Y-%m-%d")
df_proc["anio"] = df_proc["fecha_dt"].dt.year
df_proc["mes"] = df_proc["fecha_dt"].dt.month
df_proc["dia"] = df_proc["fecha_dt"].dt.day
df_proc["palabras_titulo"] = df_proc["titulo"].apply(lambda x: len(x.split()))

df_proc = df_proc.drop(columns=["fecha_dt"])

ruta_proc = os.path.join(ruta_carpeta, "mongabay_peru_procesado.csv")
df_proc.to_csv(ruta_proc, index=False, encoding="utf-8")


