"""
María Paula Valdés
Hector Aaron Pivaral
Carné: 19146
Carne: 19640
"""
from tkinter import *
from tkinter import messagebox
import modulos as md

raiz=Tk()
#raiz.config(bg=white)"
raiz.geometry("700x400")
raiz.title("Simulación de campo eléctrico 2020")
Bienvenida = Label(raiz,text= "Bienvenido a calcular campos", font="Times 20")
Bienvenida.grid(row=0, column=1, columnspan=6)

"Hola mapa ya se usar git en pycharmmm"

md.abrirventana()
md.tipo()
md.botonsimulacion()
raiz.mainloop()
