import pandas as pd
import os
import pdfkit
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import tkinter as tk
from tkinter import filedialog

# --- KONFIGURATION ---
EXPORT_DATE = datetime.now().strftime("%Y%m%d")
TEMPLATE_DIR = "templates"
OUTPUT_DIR = f"Feiertagsreport_{EXPORT_DATE}"
HTML_TEMPLATE = "report_template.html"
CSS_FILE = os.path.join(TEMPLATE_DIR, "style.css")

# Stelle sicher, dass der Output-Ordner existiert
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Jinja2 Umgebung einrichten
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
template = env.get_template(HTML_TEMPLATE)

# --- HILFSFUNKTION: Daten aus einer Zeile extrahieren ---
def extract_data(row, columns):
    return {
        "vorname": row.get(columns["vorname"], "").strip(),
        "nachname": row.get(columns["nachname"], "").strip(),
        "personalnummer": str(row.get(columns["personalnummer"], "")).strip(),
        "gearbt_feiertage": row.get(columns["gearbt_feiertage"], 0),
        "freie_feiertage": row.get(columns["freie_feiertage"], 0),
        "ausgleichstage_genommen": row.get(columns["ausgleichstage_genommen"], 0),
        "ausgleichstage_offen": row.get(columns["ausgleichstage_offen"], 0),
        "zeitraum": "01.01.2025 – 31.12.2025",
        "export_date": EXPORT_DATE
    }

# --- SPALTENMAPPING ---
columns_map = {
    "einfach": {
        "vorname": "Vorname",
        "nachname": "Nachname",
        "personalnummer": "Personalnummer",
        "gearbt_feiertage": "Gearbeitete Feiertage",
        "freie_feiertage": "Dienstfreie Feiertage",
        "ausgleichstage_genommen": "Feiertagsausgleiche",
        "ausgleichstage_offen": "Nötige Feiertagsausgleiche",
    },
    "erweitert": {
        "vorname": "Vorname",
        "nachname": "Nachname",
        "personalnummer": "Personalnummer",
        "gearbt_feiertage": "Gearbeitete Feiertage",
        "freie_feiertage": "Dienstfreie Feiertage",
        "ausgleichstage_genommen": "Feiertagsausgleiche",
        "ausgleichstage_offen": "Nötige Feiertagsausgleiche",
    }
}

# --- EXCEL VERARBEITUNG ---
def generate_reports(excel_path, version="einfach"):
    df = pd.read_excel(excel_path, sheet_name="Sheet1", skiprows=4)
    cols = columns_map[version]

    for _, row in df.iterrows():
        if pd.isna(row.get(cols["personalnummer"])):
            continue

        data = extract_data(row, cols)
        html_out = template.render(**data)

        filename = f"Feiertagsexport_{data['vorname']}_{data['nachname']}_{data['personalnummer']}_{EXPORT_DATE}.pdf"
        output_path = os.path.join(OUTPUT_DIR, filename)

        # --- HTML-Datei temporär speichern für pdfkit ---
        tmp_html_path = os.path.join(OUTPUT_DIR, "temp.html")
        with open(tmp_html_path, "w", encoding="utf-8") as f:
            f.write(html_out)

        options = {
            "enable-local-file-access": None,
            "quiet": "",
            "encoding": "UTF-8",
            "page-size": "A4",
            "margin-top": "15mm",
            "margin-bottom": "15mm",
            "margin-left": "20mm",
            "margin-right": "20mm",
            "no-outline": None
        }

        pdfkit.from_file(tmp_html_path, output_path, css=CSS_FILE, options=options)
        print(f"✅ PDF erstellt: {output_path}")

        os.remove(tmp_html_path)

# --- EINFACHE UI MIT TKINTER ---
def run_ui():
    root = tk.Tk()
    root.geometry("1000x500")
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Wähle die Feiertags-Excel-Datei",
        filetypes=[("Excel files", "*.xlsx")]
    )

    if file_path:
        version = "einfach" if "einfach" in file_path.lower() else "erweitert"
        generate_reports(file_path, version)

    root.destroy()

# --- STARTPUNKT ---
if __name__ == "__main__":
    run_ui()