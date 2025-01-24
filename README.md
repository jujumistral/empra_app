# Empra Web App

## 🚀 Projektbeschreibung

Die **Empra Web App** ist eine interaktive Webanwendung, die mit [Dash](https://dash.plotly.com/) entwickelt wurde. Sie ermöglicht die Analyse und Visualisierung von experimentellen Daten, einschließlich der Darstellung von Diagrammen, Tabellen und der Wiedergabe von Audiodateien.

Diese App wurde erstellt, um die Ergebnisse eines wissenschaftlichen Projekts zugänglicher zu machen. In unserem Fall handelt es sich dabei um ein Forschungsprojekt zur Sonifikation von EEG-Daten.
Die App bietet folgende Funktionen:
- Interaktive Visualisierungen (z. B. Boxplots und andere Diagramme)
- Experimentelle Audiodateien direkt in der App anhören
- Vergleich von Datensätzen und statistischen Ergebnissen

---

## 🛠️ Technologien

Das Projekt basiert auf folgenden Technologien:
- **Python 3.9+**
- **Dash** für die Webentwicklung
- **Plotly** für Visualisierungen
- **Pandas** für Datenverarbeitung

Zusätzliche Tools/Dateiformate:
- Audiodateien (`.wav`) zur Illustration von Ergebnissen
- CSV-Datensätze für die Analyse

---

## 📂 Projektstruktur

Hier ist die Übersicht der wichtigsten Dateien und Ordner:
empra_app/ 
├── app.py # Haupt-Skript der Dash-App 
├── assets/ # Ressourcen wie Bilder, Audiodateien, CSS 
│ ├── sounds/ # Enthält experimentelle .wav Dateien 

---

## 🌟 Installation

Führe die folgenden Schritte aus, um die App lokal auszuführen:

1. **Repository klonen**  
   Klone das Repository auf deinen lokalen Rechner:
   ```bash
   git clone https://github.com/dein-benutzername/empra_app.git
   cd empra_app
2. **Virtuelle Umgebung erstellen**
   Erstelle und aktiviere eine virtuelle Umgebung:
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
3. **Abhängigkeiten installieren**
   Installiere die benötigten Pakete:
   pip install -r requirements.txt
4. **App starten**
   Starte die App mit:
   python app.py
5. **Im Browser öffnen**
   Öffne die App im Browser unter:
   http://localhost:8050

---

## 🌐 Deployment
Die App kann über Render oder ähnliche Plattformen deployed werden. Nutze die app.py als Einstiegspunkt und achte darauf, die benötigten Dateien aus dem Ordner assets hochzuladen.

---

## ⚙️ Abhängigkeiten
Die App benötigt folgende Python-Bibliotheken, die in der Datei requirements.txt angegeben sind:
-> Dash
-> Plotly
-> Pandas
-> numpy
-> Flask (abhängig von Dash)
Installiere alle Abhängigkeiten mit:
pip install -r requirements.txt

---

## 📊 Nutzung
1. Interaktive Diagramme
Die App enthält mehrere Diagramme, die auf den hochgeladenen Datensätzen basieren und sich entsprechend der ausgewählten Bedingungen in den Dropdown-Menüs aktualisieren.
Navigiere durch die verschiedenen Registerkarten, um die Visualisierungen anzuzeigen.

2. Experimentelle Audio-Wiedergabe
Durch Auswahl der Bedingungen in den Dropdown-Menüs erfolgt auch die Auswahl der jeweiligen Audio-Datei (.wav - in unserem Fall sonifizierte EEG-Daten mit zwei verschiedenen Klangtypen).

---

## 🤝 Mitwirken
Wenn du mitwirken möchtest:

1. Forke das Repository.
2. Erstelle einen neuen Branch:
   git checkout -b feature/neuer-feature
3. Führe Änderungen durch und committe sie:
   git commit -m "Feature hinzugefügt"
4. Push den Branch und erstelle einen Pull-Request.

---

## 📜 Lizenz
Dieses Projekt steht unter der MIT-Lizenz. Siehe die LICENSE-Datei für weitere Informationen.
