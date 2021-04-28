#!/usr/bin/env python
#-*- coding: utf-8 -*-

from tkinter import *

raiz = Tk()

def hola():
    print("Hola!")

# Crear un menu popup (emergente)
menu = Menu(raiz, tearoff=0)
menu.add_command(label="Undo", command=hola)
menu.add_command(label="Redo", command=hola)

# Crear un marco
marco = Frame(raiz, width=512, height=512)
marco.pack()

def popup(event):
    menu.post(event.x_root, event.y_root)

# Enlazar el menu popup al marco
marco.bind("<Button-3>", popup)

# Mostrar la ventana
raiz.mainloop()