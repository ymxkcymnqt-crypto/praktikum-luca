# 🍎 Kalorienrechner – Python Übung für Einsteiger

## Einleitung

In dieser Übung baust du einen **Kalorienrechner**, mit dem man Mahlzeiten mit Kalorienangaben erfassen und eine Tageszusammenfassung anzeigen kann. Die App hat eine grafische Oberfläche (GUI) mit **Tkinter**.

**Du musst nur die Logik-Methoden in der Klasse `MealTracker` implementieren.** Die grafische Oberfläche ist bereits fertig programmiert und ruft deine Methoden auf.

---

## Lernziele

Nach dieser Übung kannst du:

- Mit **Listen** (`list`) und **Dictionaries** (`dict`) arbeiten
- **Schleifen** (`for`) und **f-Strings** verwenden
- Eine einfache **Klasse** mit Methoden schreiben
- **Unit Tests** ausführen und verstehen
- Den grundlegenden Aufbau einer **Tkinter-GUI** nachvollziehen

---

## Wichtige Konzepte: Was ist eine Klasse?

In diesem Projekt arbeitest du mit **Klassen**. Eine Klasse ist ein zentrales Konzept in Python (und vielen anderen Programmiersprachen). Hier eine kurze Erklärung:

**Stell dir eine Klasse wie einen Bauplan vor.** Ein Bauplan für ein Haus beschreibt, wie das Haus aussehen soll (Räume, Türen, Fenster) und was man darin tun kann (kochen, schlafen). Aus einem Bauplan kann man viele Häuser bauen – jedes ist ein eigenes **Objekt**.

```python
# Die Klasse (= der Bauplan)
class MealTracker:
    def __init__(self):          # Wird beim Erstellen aufgerufen
        self.meals = []          # Jedes Objekt hat seine eigene Mahlzeiten-Liste

    def add_meal(self, name, calories):   # Eine Methode (= Funktion in einer Klasse)
        ...

# Ein Objekt erstellen (= ein Haus nach dem Bauplan bauen)
tracker = MealTracker()

# Methoden aufrufen (= etwas im Haus tun)
tracker.add_meal("Frühstück", 450)
```

Wichtige Begriffe:
- **Klasse** (`class`): Der Bauplan
- **Objekt / Instanz**: Ein konkretes Exemplar, das nach dem Bauplan erstellt wurde
- **Attribut** (`self.meals`): Daten, die zu einem Objekt gehören
- **Methode** (`add_meal`, `reset_day`): Funktionen, die zu einer Klasse gehören
- **`self`**: Bezieht sich immer auf das aktuelle Objekt – damit kann jedes Objekt auf seine eigenen Daten zugreifen
- **`__init__`**: Die spezielle Methode, die automatisch aufgerufen wird, wenn ein neues Objekt erstellt wird

### Weiterführende Literatur

- 📖 [Python-Dokumentation: Klassen (deutsch)](https://docs.python.org/de/3/tutorial/classes.html)
- 📖 [Real Python: Object-Oriented Programming (englisch)](https://realpython.com/python3-object-oriented-programming/)
- 📖 [W3Schools: Python Classes (englisch, einsteigerfreundlich)](https://www.w3schools.com/python/python_classes.asp)
- 📖 [Python-Dokumentation: Tkinter (englisch)](https://docs.python.org/3/library/tkinter.html)

---

## Voraussetzungen

- **Python 3** (Version 3.8 oder neuer)
- **Tkinter** – ist bei Python bereits dabei, muss nicht installiert werden
- Ein Texteditor oder IDE (z.B. VS Code)
- Ein Terminal / eine Kommandozeile

---

## Projektstruktur

```
calories_calculator/
├── calories_calculator.py          ← Hier arbeitest du! (MealTracker + GUI)
├── test_calories.py                ← Unit Tests (bereits fertig)
├── calories_calculator_solution.py ← Lösung (NICHT anschauen!)
└── README.md                       ← Diese Datei
```

---

## So startest du

### Tests ausführen (werden am Anfang alle fehlschlagen):
```bash
python -m unittest test_calories.py -v
```

**Was sind Tests?**
Tests sind kleine Programme, die automatisch prüfen, ob dein Code richtig funktioniert. Stell dir vor, du hast eine Methode geschrieben, die zwei Zahlen addieren soll. Ein Test würde dann z.B. prüfen: *„Wenn ich 3 und 5 eingebe, kommt dann wirklich 8 heraus?"*

In dieser Übung sind **16 Tests** bereits für dich geschrieben (in der Datei `test_calories.py`). Jeder Test ruft eine deiner Methoden auf und prüft, ob das Ergebnis stimmt. Am Anfang werden alle Tests **fehlschlagen** (rot ❌), weil deine Methoden noch nicht implementiert sind. Mit jeder Aufgabe, die du löst, werden mehr Tests **bestehen** (grün ✅).

Das Prinzip dahinter heißt **Test-Driven Development (TDD)**: Die Tests existieren *bevor* der eigentliche Code geschrieben wird. Dein Ziel ist es, den Code so zu schreiben, dass alle Tests grün werden.

Die Ausgabe `-v` (verbose) zeigt dir jeden einzelnen Test mit seinem Ergebnis:
```
test_add_single_meal (test_calories.TestAddMeal) ... ok       ← ✅ bestanden
test_total_no_meals (test_calories.TestGetTotalCalories) ... FAIL  ← ❌ noch nicht implementiert
```

### App starten (GUI wird geöffnet, funktioniert aber noch nicht richtig):
```bash
python calories_calculator.py
```

---

## Aufgaben

### Aufgabe 1: Code lesen und verstehen

**Ziel:** Verstehe den Aufbau des Projekts, bevor du mit dem Programmieren anfängst.

**Schritte:**

1. Öffne die Datei `calories_calculator.py` in deinem Editor.
2. Lies die Kommentare am Anfang der Datei – sie erklären, was die App tun soll.
3. Schau dir die Klasse `MealTracker` an. Sie hat vier Methoden, die du implementieren musst. Jede Methode hat einen ausführlichen Docstring (Kommentar), der erklärt:
   - Was die Methode tun soll
   - Welche Parameter sie bekommt
   - Was sie zurückgeben soll
   - Einen Hinweis, wie du sie implementieren kannst
   - Ein Beispiel
4. Scrolle weiter zur Klasse `CaloriesApp`. Das ist die grafische Oberfläche. **Du musst diesen Teil nicht ändern**, aber lies die Kommentare durch, um zu verstehen, wie die GUI aufgebaut ist. Achte besonders auf:
   - Wie Widgets (Label, Entry, Button, Listbox) erstellt werden
   - Wie `grid()` die Widgets im Fenster anordnet
   - Wie `command=self._on_add_meal` einen Button mit einer Methode verknüpft
   - Wie `StringVar` genutzt wird, um ein Label automatisch zu aktualisieren

5. Öffne die Datei `test_calories.py` und lies die ersten Kommentare. Verstehe, was ein Unit Test ist und wie man die Tests ausführt.

> **Tipp:** Nimm dir ruhig 15-20 Minuten Zeit zum Lesen. Je besser du den Code verstehst, desto leichter werden die nächsten Aufgaben.

---

### Aufgabe 2: `add_meal()` implementieren

**Ziel:** Speichere eine Mahlzeit in der internen Liste.

**Was du wissen musst:**
- Ein **Dictionary** (kurz: `dict`) speichert Schlüssel-Wert-Paare:
  ```python
  meal = {"name": "Frühstück", "calories": 450}
  print(meal["name"])       # gibt "Frühstück" aus
  print(meal["calories"])   # gibt 450 aus
  ```
  📖 Mehr dazu: [Python-Dokumentation: Dictionaries (deutsch)](https://docs.python.org/de/3/tutorial/datastructures.html#dictionaries) | [W3Schools: Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)

- Eine **Liste** kann mit `.append()` erweitert werden:
  ```python
  my_list = []
  my_list.append("Hallo")   # my_list ist jetzt ["Hallo"]
  ```
  📖 Mehr dazu: [Python-Dokumentation: Listen (deutsch)](https://docs.python.org/de/3/tutorial/datastructures.html#more-on-lists) | [W3Schools: Python Lists](https://www.w3schools.com/python/python_lists.asp)

**Schritte:**

1. Öffne `calories_calculator.py` und finde die Methode `add_meal()`.
2. Lösche die Zeile `pass`.
3. Erstelle ein Dictionary mit den Schlüsseln `"name"` und `"calories"`.
4. Hänge das Dictionary an `self.meals` an.

**Zugehörige Tests:** `TestAddMeal` (5 Tests)

**Prüfe deinen Fortschritt:**
```bash
python -m unittest test_calories.TestAddMeal -v
```
Wenn alle 5 Tests grün ("ok") sind, hast du die Aufgabe richtig gelöst! ✅

---

### Aufgabe 3: `get_total_calories()` implementieren

**Ziel:** Berechne die Summe aller Kalorien.

**Was du wissen musst:**
- Eine **for-Schleife** geht alle Elemente einer Liste durch:
  ```python
  for item in my_list:
      print(item)
  ```
- Du kannst auf einen Dictionary-Wert mit eckigen Klammern zugreifen:
  ```python
  meal = {"name": "Lunch", "calories": 700}
  print(meal["calories"])   # gibt 700 aus
  ```

**Schritte:**

1. Finde die Methode `get_total_calories()`.
2. Lösche die Zeile `pass`.
3. Erstelle eine Variable `total` und setze sie auf `0`.
4. Gehe mit einer for-Schleife durch `self.meals`.
5. Addiere bei jedem Durchlauf die Kalorien zu `total`.
6. Gib `total` mit `return` zurück.

**Zugehörige Tests:** `TestGetTotalCalories` (4 Tests)

**Prüfe deinen Fortschritt:**
```bash
python -m unittest test_calories.TestGetTotalCalories -v
```

---

### Aufgabe 4: `get_meals_summary()` implementieren

**Ziel:** Erstelle eine Liste von formatierten Zusammenfassungs-Strings.

**Was du wissen musst:**
- Ein **f-String** erlaubt es, Variablen direkt in einen Text einzubauen:
  ```python
  name = "Frühstück"
  cals = 450
  text = f"{name} - {cals} kcal"   # ergibt: "Frühstück - 450 kcal"
  ```

**Schritte:**

1. Finde die Methode `get_meals_summary()`.
2. Lösche die Zeile `pass`.
3. Erstelle eine leere Liste `summary = []`.
4. Gehe mit einer for-Schleife durch `self.meals`.
5. Erstelle für jede Mahlzeit einen f-String im Format: `"Name - Kalorien kcal"`
6. Hänge den String an `summary` an.
7. Gib `summary` mit `return` zurück.

**Wichtig:** Das Format muss exakt so sein: `"Breakfast - 450 kcal"` (mit Leerzeichen und "kcal"). Die Tests prüfen das genaue Format!

**Zugehörige Tests:** `TestGetMealsSummary` (4 Tests)

**Prüfe deinen Fortschritt:**
```bash
python -m unittest test_calories.TestGetMealsSummary -v
```

---

### Aufgabe 5: `reset_day()` implementieren

**Ziel:** Lösche alle Mahlzeiten (neuer Tag).

**Was du wissen musst:**
- Eine Liste kann so geleert werden:
  ```python
  my_list.clear()     # entfernt alle Einträge
  # oder:
  my_list = []        # ersetzt die Liste mit einer neuen, leeren Liste
  ```

**Schritte:**

1. Finde die Methode `reset_day()`.
2. Lösche die Zeile `pass`.
3. Leere die Liste `self.meals`.

**Zugehörige Tests:** `TestResetDay` (3 Tests)

**Prüfe deinen Fortschritt:**
```bash
python -m unittest test_calories.TestResetDay -v
```

---

### Aufgabe 6: Alle Tests ausführen

**Ziel:** Stelle sicher, dass alle 16 Tests bestanden werden.

**Schritte:**

1. Führe alle Tests aus:
   ```bash
   python -m unittest test_calories.py -v
   ```
2. Du solltest diese Ausgabe sehen:
   ```
   test_add_meal_preserves_order (test_calories.TestAddMeal) ... ok
   test_add_meal_stores_correct_calories (test_calories.TestAddMeal) ... ok
   test_add_meal_stores_correct_name (test_calories.TestAddMeal) ... ok
   test_add_multiple_meals (test_calories.TestAddMeal) ... ok
   test_add_single_meal (test_calories.TestAddMeal) ... ok
   test_total_multiple_meals (test_calories.TestGetTotalCalories) ... ok
   test_total_no_meals (test_calories.TestGetTotalCalories) ... ok
   test_total_single_meal (test_calories.TestGetTotalCalories) ... ok
   test_total_with_zero_calorie_meal (test_calories.TestGetTotalCalories) ... ok
   test_summary_multiple_meals (test_calories.TestGetMealsSummary) ... ok
   test_summary_no_meals (test_calories.TestGetMealsSummary) ... ok
   test_summary_returns_list (test_calories.TestGetMealsSummary) ... ok
   test_summary_single_meal_format (test_calories.TestGetMealsSummary) ... ok
   test_reset_clears_meals (test_calories.TestResetDay) ... ok
   test_reset_then_add_new_meal (test_calories.TestResetDay) ... ok
   test_reset_then_total_is_zero (test_calories.TestResetDay) ... ok

   ----------------------------------------------------------------------
   Ran 16 tests in 0.001s

   OK
   ```
3. Wenn ein Test fehlschlägt, lies die Fehlermeldung genau durch. Sie zeigt dir:
   - Welcher Test fehlgeschlagen ist
   - Was erwartet wurde (`Expected`)
   - Was tatsächlich herauskam (`Got` oder `Actual`)

---

### Aufgabe 7: App starten und manuell testen

**Ziel:** Teste die App über die grafische Oberfläche.

**Schritte:**

1. Starte die App:
   ```bash
   python calories_calculator.py
   ```
2. Es öffnet sich ein Fenster mit Eingabefeldern, Buttons und einer Liste.
3. Teste folgendes:
   - Gib "Frühstück" und "450" ein, klicke "Add Meal" → Die Mahlzeit erscheint in der Liste
   - Gib "Mittagessen" und "700" ein, klicke "Add Meal" → Zweite Mahlzeit in der Liste
   - Das "Total"-Label sollte "Total: 1150 kcal" anzeigen
   - Klicke "Reset Day" und bestätige → Liste ist leer, Total ist 0

---

## Bonusaufgaben

Die folgenden Aufgaben sind optional und etwas schwieriger. Sie erfordern, dass du den **Tkinter-Code** der `CaloriesApp`-Klasse veränderst.

---

### Bonusaufgabe 1: Eingabevalidierung verbessern

**Ziel:** Zeige dem Benutzer hilfreiche Fehlermeldungen bei ungültigen Eingaben.

> **Hinweis:** Die grundlegende Validierung ist bereits in der GUI-Klasse eingebaut (`_on_add_meal`-Methode). Für diese Bonusaufgabe kannst du die Validierung auch in die `MealTracker`-Klasse selbst einbauen, sodass sie auch ohne GUI greift.

**Schritte:**

1. Ändere `add_meal()` so, dass die Methode `False` zurückgibt, wenn:
   - `name` leer ist (leerer String `""` oder nur Leerzeichen)
   - `calories` negativ ist (kleiner als 0)
2. Wenn die Eingabe gültig ist, soll die Methode `True` zurückgeben.
3. Teste deine Änderung manuell in der App.

---

### Bonusaufgabe 2: "Mahlzeit löschen"-Button

**Ziel:** Füge einen Button hinzu, mit dem man eine ausgewählte Mahlzeit aus der Liste entfernen kann.

**Hinweise:**

1. Füge in `MealTracker` eine neue Methode `delete_meal(self, index)` hinzu:
   ```python
   def delete_meal(self, index):
       """Delete a meal at the given list index."""
       if 0 <= index < len(self.meals):
           self.meals.pop(index)
   ```

2. In der `CaloriesApp`-Klasse, schau dir an, wie der "Reset Day"-Button erstellt wird. Erstelle auf die gleiche Art einen neuen Button "Delete Selected".

3. Der Button soll eine neue Methode `_on_delete()` aufrufen. Diese Methode:
   - Liest die aktuelle Auswahl der Listbox: `selection = self.listbox.curselection()`
   - `curselection()` gibt ein Tuple zurück, z.B. `(2,)` wenn der dritte Eintrag ausgewählt ist
   - Wenn nichts ausgewählt ist, zeige eine Fehlermeldung
   - Rufe `self.tracker.delete_meal(selection[0])` auf
   - Aktualisiere die Anzeige mit `self._refresh_display()`

---

### Bonusaufgabe 3: Die GUI verschönern

**Ziel:** Ändere Farben, Schriftarten oder das Layout der App.

**Hinweise:**

- **Hintergrundfarbe** ändern:
  ```python
  self.root.configure(bg="#f0f0f0")  # Hellgrau
  ```

- **Schriftart** eines Labels ändern:
  ```python
  tk.Label(self.root, text="Hallo", font=("Helvetica", 16, "bold"))
  ```

- **Button-Farbe** ändern:
  ```python
  tk.Button(self.root, text="Klick", bg="#4CAF50", fg="white")
  # bg = Hintergrundfarbe (background), fg = Textfarbe (foreground)
  ```

- **Listbox-Farbe** ändern:
  ```python
  self.listbox.configure(bg="#ffffcc", font=("Courier", 11))
  ```

**Schritte:**

1. Wähle ein Farbschema, das dir gefällt (z.B. auf https://coolors.co).
2. Ändere die Hintergrundfarbe des Fensters.
3. Ändere die Schriftart der Labels und Buttons.
4. Ändere die Farben der Listbox.
5. Experimentiere! Du kannst nichts kaputt machen – wenn etwas nicht funktioniert, mache die Änderung einfach rückgängig.

---

## Beispiel-Interaktion

So sollte die App aussehen, wenn alles funktioniert:

```
┌─────────────────────────────────────┐
│         Calories Calculator         │
├─────────────────────────────────────┤
│  Meal name:   [ Frühstück        ]  │
│  Calories:    [ 450              ]  │
│                                     │
│          [ Add Meal ]               │
│                                     │
│  Today's Meals:                     │
│  ┌─────────────────────────────┐    │
│  │ Frühstück - 450 kcal        │    │
│  │ Mittagessen - 700 kcal      │    │
│  │ Snack - 150 kcal            │    │
│  │                             │    │
│  └─────────────────────────────┘    │
│                                     │
│        Total: 1300 kcal             │
│                                     │
│         [ Reset Day ]               │
└─────────────────────────────────────┘
```

---

## Hilfe

Falls du nicht weiterkommst:

1. **Lies die Fehlermeldung genau durch** – Python sagt dir meistens genau, was falsch ist.
2. **Lies den Docstring der Methode nochmal** – dort stehen Hinweise und Beispiele.
3. **Nutze `print()`** zum Debuggen:
   ```python
   def add_meal(self, name, calories):
       print(f"Adding meal: {name} with {calories} calories")
       # ... dein Code ...
       print(f"Meals list is now: {self.meals}")
   ```
4. **Frage deinen Betreuer** – lieber einmal zu viel fragen als eine Stunde feststecken!

> ⚠️ **Die Datei `calories_calculator_solution.py` enthält die vollständige Lösung. Schau dort nur rein, wenn du wirklich nicht weiterkommst und es mit deinem Betreuer besprochen hast.**

---

Viel Erfolg! 🚀
