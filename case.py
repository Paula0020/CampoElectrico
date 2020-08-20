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
#raiz.config(bg=white)"
raiz.geometry("700x400")
raiz.title("Simulación de campo eléctrico 2020")
#raiz.configure(width=200,height=100)
#raiz.grid(padx=600, pady=600)


md.bienvenida()
md.abrirventana()
md.tipo()
md.botonsimulacion()
raiz.mainloop()
