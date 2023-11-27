# Aufgabenverteilung

1. Darstellung einer Markov Kette bezogen auf unser Beispiel (kontinuierlich)


# Stichpunkte für Präsentation

## Einsatzzweck

### Hintergrund
- Benannt nach dem Mathematiker Andrei Markow (1856-1922).
- Anwendung im Risikomanagement.

### Fehlermöglichkeits- und Einflussanalyse (FMEA)
#### Stärken
- Vollumfassende Betrachtung des Systems durch Zerlegung in kleinste Komponenten.
- ISO-Regelwerke beschreiben FMEA.
- Klare Formalisierung mithilfe von "Worksheets."

#### Grenzen
- Mathematische Herausforderungen bei der Multiplikation ordinal skalierter Merkmale.
- Begrenzte Bewertungsmöglichkeiten für bestimmte Risiken.
- Zeit- und Ressourcenverbrauch.
- Großer Datenbedarf und Systemkenntnisse erforderlich.
- Interdependenzen können in der ursprünglichen FMEA nicht analysiert werden.

### Markov-Analyse
- Modellierung zufälliger Zustandsänderungen ("Random Walk").
- Anwendung bei Prozessen mit begrenztem zeitlichen Einfluss oder Gedächtnislosigkeit.
- Analytische Ermittlung von Ausfall- und Verfügbarkeitswahrscheinlichkeiten.
- Hauptsächlich für wiederholende, komplexe, zufällig beeinflusste Prozesse.
- Unterscheidung zwischen kontinuierlichen und diskreten Markov-Prozessen.
- Markov-Ketten als diskrete Prozesse, bei denen der Zustand nur vom vorherigen Schritt abhängt.

### Stärken der Markov-Analyse
- Präzise Aussagen über Ausfallwahrscheinlichkeiten, auch bei starken Abhängigkeiten zwischen Teilprozessen.
- Häufig verwendetes Modell zur Beschreibung von Systemen mit zufälligen Zustandsübergängen.

## Beschreibung

### Einführung
- Markov-Prozess als Grundlage für Verlässlichkeitsprüfung
- Modellierung in Form einer Markov-Kette
- Beschreibung der zeitlichen Entwicklung von Objekten oder Systemen

### Modellierungskomponenten
1. **Zustandsraum:**
   - Endliche Menge möglicher Zustände

2. **Anfangsverteilung:**
   - Wahrscheinlichkeiten zu Beginn in bestimmten Zuständen

3. **Übergangsmatrix:**
   - Matrix mit Übergangswahrscheinlichkeiten zwischen Zuständen

### Markov-Ketten
- Zustand abhängig nur vom unmittelbaren Vorgänger
- Migrationsmatrix beschreibt Wahrscheinlichkeiten der Zustandsänderung

### Anwendungsbereiche
- Beispiel: Ratingmigrationen von Unternehmen
- Evaluierung der zeitlichen Entwicklung von Projekten

### Berechnungen und Ergebnisse
- Stationäre Wahrscheinlichkeiten
- Präzise Berechnung der Ausfallwahrscheinlichkeit komplexer Systeme

### Klassische Beispiele
- "Zufällige Irrfahrten" oder "Random Walks"
- Anwendungen in der Finanzmathematik (z.B., Black/Scholes-Formel)

### Schlussfolgerung
- Markov-Ketten als mathematische Grundlage für die Modellierung zeitlicher Systementwicklungen
- Vielseitige Anwendungen in verschiedenen Bereichen
