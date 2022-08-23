import json
import tkinter as tk
from tkinter import ttk
import math

alc_vol = 0

def oblicz_objetosc():
    for bottle in alko:
        if bottle["name"].lower() == current_bottle.get().lower():
            print("2")
            density = (bottle["full_weight"] - bottle["empty_weight"]) / bottle["volume"]
            alcohol_weight = (int(current_weight.get()) - bottle["empty_weight"])
            global alc_vol
            alc_vol = math.trunc(alcohol_weight / density)
            volume_display.config(text=f"{alc_vol} ml")


# ------- initial load --------
alcohols = open('alcohols.json', 'r')
alko = json.load(alcohols)
lista_butli =[]
for bottle in alko:
    lista_butli.append(bottle["name"])

## --------- window ------
window = tk.Tk()
window.title("Bar Inventory by Q")
window.config(padx=30, pady=30)
canvas = tk.Canvas(width=140, height=40)
canvas.grid(column=2, row=1)
#  labels
butla_label = tk.Label(text="Butelka:")
butla_label.grid(column=1, row=0)
waga_label = tk.Label(text="Waga w gramach")
waga_label.grid(column=2, row=0)
# Combobox creation
chosenbottle = tk.StringVar()
current_bottle = ttk.Combobox(window, textvariable=chosenbottle, width=27, state="readonly")
current_bottle['values'] = lista_butli
current_bottle.grid(column=1, row=1)
# inputs
current_weight = ttk.Entry(width = 45)
current_weight.grid(column=2, row=1)

volume_display_label = tk.Label(height=5, width=20)
volume_display_label.config(text="W butelce:")
volume_display_label.grid(column=1, row=3)
volume_display = tk.Label(height=5, width=20)
volume_display.config(text=0)
volume_display.grid(column=2, row=3)

akceptuj_button = tk.Button(text="Ok")
akceptuj_button.config(command=oblicz_objetosc)
akceptuj_button.grid(column=3, row=1)

window.mainloop()