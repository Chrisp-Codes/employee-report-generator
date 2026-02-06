# Holiday Report Generator

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Build](https://img.shields.io/badge/build-pdfkit%20%2B%20wkhtmltopdf-success)
![Status](https://img.shields.io/badge/status-beta-yellow)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
[![English](https://img.shields.io/badge/README-English-informational?style=flat-square)](README_en.md)

---

## Overview

The **Holiday Report Generator** is a Python-based application that creates personalized PDF reports for employees based on Excel input files.  
Designed for HR departments, it runs as a standalone executable (`.exe`) and requires no technical knowledge from end users.

---

## Objectives

- Automate generation of individual reports for employees
- Provide a GUI-based solution that requires no installations
- Export well-formatted PDF documents using HTML & CSS templates
- Enable fully offline usage for security-sensitive environments

---

## Features

- Excel file selection via graphical interface (tkinter)
- Automatic processing of all employee records
- Template-based rendering using Jinja2
- Custom layout using external CSS
- One PDF per employee, named and saved in a dedicated folder

---

## Project Structure

```text
.
├── ft_report.py                  # Main Python script
├── style.css                    # Styling for the report
├── templates/
│   └── report_template.html     # HTML report template
├── bin/
│   └── wkhtmltopdf.exe          # PDF renderer (not included in repo)
└── dist/
    └── HolidayReport.exe        # Compiled app (optional)
