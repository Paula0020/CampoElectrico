"""
María Paula Valdés
Hector Aaron Pivaral
Carné: 19146
Carne: 19640
"""
import tkinter as tk
from tkinter import *
from tkinter import messagebox
root = Tk()

velocidad=0
Intensidad=0
masa=0
carga=0

def particulas(m,c):
    print(str(m))
    print(str(c))
    m= masa
    c=carga
def validateV_float(var):
    new_value = var.get()
    try:
        new_value == float(new_value)
        velocidad = new_value
        print(velocidad)
    except:
        messagebox.showinfo(title="Cuidado", message="Datos no válidos")

def validateI_float(var):
    new_value = var.get()
    try:
        new_value == float(new_value)
        Intensidad = new_value
        return(Intensidad)
    except:
        messagebox.showinfo(title="Cuidado", message="Datos no válidos")

    

