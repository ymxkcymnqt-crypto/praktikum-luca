# tkinter importieren für die grafische Benutzeroberfläche
import tkinter as tk
expression = ""
def on_button_click(value):
    global expression

    if value == "C":
        display.delete(0, tk.END)  # löscht alles
        expression = ""
        return

    if value == "=":
        try:
            result = str(eval(expression))
            display.delete(0, tk.END)
            display.insert(0, result)
            expression = result
        except Exception:
            display.delete(0, tk.END)
            display.insert(0, "Fehler")
            expression = ""
        return

    expression += value
    display.insert(tk.END, value) 

# Hauptfenster erstellen und Titel setzen
root = tk.Tk()
root.title("Einfacher Taschenrechner")
# Eingabefeld (Display) oben im Fenster anlegen
# Erstreckt sich über alle 4 Spalten (columnspan=4)
display = tk.Entry(root, width=30, borderwidth=5, justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button-Beschriftungen in der Reihenfolge des 4x4-Rasters
buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','C','=','+'
]

# Startposition für die Buttons (Zeile 1, da Zeile 0 = Display)
row = 1
col = 0

# Buttons erzeugen und im Grid platzieren
for button in buttons:
    # Lambda mit Default-Argument, damit jeder Button seinen eigenen Wert behält
    action = lambda x=button: on_button_click(x)
    tk.Button(root, text=button, width=5, height=2, command=action).grid(row=row, column=col, padx=5, pady=5)

    # Zur nächsten Spalte wechseln; nach 4 Spalten neue Zeile beginnen
    col += 1
    if col > 3:
        col = 0
        row += 1

# Tkinter-Event-Loop starten (Fenster bleibt offen bis es geschlossen wird)
root.mainloop()
