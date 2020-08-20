"""
María Paula Valdés
Hector Aaron Pivaral
Carné: 19146
Carne:
"""
from tkinter import *
from tkinter import messagebox
import modulos as md

raiz=Tk()
"raiz.config(bg=white)"
raiz.geometry("800x600")
raiz.title("Campo Eléctrico")


md.bienvenida()
md.abrirventana()
md.tipo()
md.botonsimulacion()
raiz.mainloop()
