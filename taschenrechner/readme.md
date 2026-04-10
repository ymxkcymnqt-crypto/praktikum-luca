# Praktikum: Einfacher Taschenrechner mit Python & Tkinter

## 1. Entwicklungsumgebung einrichten

### 1.1 Projekt anlegen

1. Erstelle einen neuen Ordner für das Projekt, z. B. `taschenrechner_praktikum`.
2. Öffne den Ordner in VS Code: **Datei → Ordner öffnen…**
3. Erstelle eine neue Datei: **Datei → Neue Datei** → speichere als `calculator.py`.
4. Wähle den Python-Interpreter aus:
   - Drücke `Strg+Shift+P` → tippe **"Python: Select Interpreter"** → wähle deine Python-Installation aus.

### 1.1 Programm ausführen

- Drücke `F5` oder klicke oben rechts auf das **▶ Play-Symbol**.
- Alternativ im Terminal:
  ```bash
  python calculator.py
  ```

---

## 2. Projektbeschreibung

Du sollst einen einfachen Taschenrechner mit grafischer Oberfläche (GUI) bauen. Dafür verwenden wir **Tkinter**, das in Python bereits enthalten ist — es muss nichts extra installiert werden.

Der Taschenrechner soll folgendes können:

- Die vier Grundrechenarten: **Addition (+), Subtraktion (-), Multiplikation (*), Division (/)**
- Eine **Anzeige** (Display), die die Eingabe und das Ergebnis zeigt
- Einen **C-Button** zum Löschen der Eingabe
- Einen **=-Button** zum Berechnen des Ergebnisses

---

## 3. Grundgerüst (vorgegeben)

Der folgende Code ist bereits vorgegeben. Er erstellt das Fenster, das Display und die Buttons. Deine Aufgabe ist es, die Funktion `on_button_click()` zu implementieren.

```python
import tkinter as tk

def on_button_click(value):
    # TODO: Hier muss die Logik implementiert werden
    pass

root = tk.Tk()
root.title("Einfacher Taschenrechner")

display = tk.Entry(root, width=30, borderwidth=5, justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','C','=','+'
]

row = 1
col = 0

for button in buttons:
    action = lambda x=button: on_button_click(x)
    tk.Button(root, text=button, width=5, height=2, command=action)\
        .grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
```

---

## 4. Aufgaben

### Aufgabe 1: Ziffern und Operatoren ins Display schreiben

**Ziel:** Wenn eine Zahl (`0–9`) oder ein Operator (`+`, `-`, `*`, `/`) gedrückt wird, soll der Wert ans Ende des Displays angehängt werden.

**Hinweise:**
- `display.get()` gibt den aktuellen Text im Display zurück.
- `display.insert(tk.END, text)` fügt Text am Ende ein.

**Teste:** Drücke nacheinander `1`, `+`, `2`. Im Display sollte `1+2` stehen.

---

### Aufgabe 2: C-Button — Display löschen

**Ziel:** Wenn `C` gedrückt wird, soll das Display komplett geleert werden.

**Hinweise:**
- `display.delete(0, tk.END)` löscht den gesamten Inhalt.

**Teste:** Gib etwas ein, drücke `C`. Das Display sollte leer sein.

---

### Aufgabe 3: =-Button — Ergebnis berechnen

**Ziel:** Wenn `=` gedrückt wird, soll der Ausdruck im Display berechnet und das Ergebnis angezeigt werden.

**Hinweise:**
- `eval(ausdruck)` kann einen mathematischen Ausdruck als String auswerten, z. B. `eval("1+2")` ergibt `3`.
- Zuerst den aktuellen Text holen, dann das Display leeren, dann das Ergebnis einfügen.

**Teste:** Gib `10+5` ein und drücke `=`. Das Display sollte `15` anzeigen.

---

### Aufgabe 4: Fehlerbehandlung

**Ziel:** Wenn ein ungültiger Ausdruck eingegeben wird (z. B. `1++2` oder `abc`), soll im Display **"Fehler"** angezeigt werden, statt dass das Programm abstürzt.

**Hinweise:**
- Verwende `try` / `except`, um Fehler bei `eval()` abzufangen.

**Teste:** Gib `5//` ein und drücke `=`. Statt eines Absturzes sollte "Fehler" erscheinen.

---

### Aufgabe 5: Division durch Null abfangen

**Ziel:** Wenn durch Null geteilt wird (z. B. `5/0`), soll eine sinnvolle Meldung erscheinen, z. B. **"Div/0!"**.

**Hinweise:**
- `ZeroDivisionError` ist eine spezielle Exception in Python.
- Du kannst mehrere `except`-Blöcke verwenden.

**Teste:** Gib `5/0` ein und drücke `=`. Es sollte "Div/0!" erscheinen.

---

### Aufgabe 6: Dezimalzahlen

**Ziel:** Füge einen `.`-Button hinzu, damit auch Dezimalzahlen wie `3.14` eingegeben werden können.

**Hinweise:**
- Erweitere die `buttons`-Liste um einen `.`-Button.
- Überlege, wo im Raster der Button hin soll (z. B. `'0'` schmaler machen oder Layout anpassen).

---

## 5. Struktur der Funktion `on_button_click()`

Wenn du nicht weißt, wo du anfangen sollst, orientiere dich an dieser Struktur:

```python
def on_button_click(value):
    if value == 'C':
        # Display leeren
        ...
    elif value == '=':
        # Ausdruck berechnen
        ...
    else:
        # Ziffer oder Operator ins Display schreiben
        ...
```

---

