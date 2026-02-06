# Feiertagsreport Generator

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Build](https://img.shields.io/badge/build-pdfkit%20%2B%20wkhtmltopdf-success)
![Status](https://img.shields.io/badge/status-beta-yellow)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
[![Deutsch](https://img.shields.io/badge/README-Deutsch-informational?style=flat-square)](README.md)

---

## Übersicht

Der **Feiertagsreport Generator** ist ein Python-basiertes Tool zur automatisierten Erstellung individueller PDF-Reports für Mitarbeitende auf Basis einer Excel-Eingabedatei. Die Anwendung richtet sich insbesondere an HR-Abteilungen und bietet eine einfache grafische Benutzeroberfläche für die Verarbeitung – ohne technische Vorkenntnisse und ohne Installation zusätzlicher Software beim Endnutzer.

---

## Zielsetzung

- Automatisierte Auswertung von Feiertagsdaten je Mitarbeitendem
- Einfache Anwendung über eine ausführbare `.exe`-Datei
- Personalisierte PDF-Reports im Corporate-Layout
- Kein technisches Know-how auf Kundenseite erforderlich
- Lokale Ausführung ohne Internetverbindung

---

## Funktionen

- Auswahl einer Excel-Datei über grafische Oberfläche (`tkinter`)
- Automatische Verarbeitung aller enthaltenen Datensätze
- Rendering eines HTML-Templates mit individuellen Platzhaltern
- Formatierung mittels zentraler CSS-Datei
- Erzeugung eines PDF-Dokuments je Mitarbeitendem
- Ablage im Output-Ordner `Feiertagsreport_<YYYYMMDD>/`

---

## Projektstruktur

```text
.
├── ft_report.py                  # Hauptskript
├── style.css                    # Zentrales Layout für den Report
├── templates/
│   └── report_template.html     # HTML-Template mit Platzhaltern
├── bin/
│   └── wkhtmltopdf.exe          # PDF-Konverter (nicht im Repo enthalten)
└── dist/
    └── Feiertagsreport.exe      # Kompilierte Anwendung (optional)
