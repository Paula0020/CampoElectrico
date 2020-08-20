"""
María Paula Valdés
Hector Aaron Pivaral
Carné: 19146
Carne:
"""
import tkinter as tk
from tkinter import *
"from tkinter import messagebox"


def bienvenida():
    Bienvenida = Label(text= "Bienvenido a calcular campos", font="Times 20")
    Bienvenida.grid(row=0, column=1, columnspan=6)

def abrirventana():
    label= tk.Label(text="Intesidad de campo", font= "Cambria 13")
    label.grid(row=1,column=0)
    entrada= tk.Entry(width=10, font= "Cambria 12")
    entrada.grid(row=2,column=0)
    
    label2= tk.Label(text="Velocidad de particula", font= "Cambria 13")
    label2.grid(row=1,column=1)
    entrada2= tk.Entry(width=10, font= "Cambria 12")
    entrada2.grid(row=2,column=1)

def tipo():
    label3= tk.Label(text="Tipo de particula", font= "Cambria 15")
    label3.grid(row=1, column=2, columnspan=4)
     # electrón, positrón, protón, neutrón, partícula alfa, núcleo de deuterio, muón,
    TIP= [
        ("Proton","1"),
        ("Electron","2"),
        ("Neutron","3"),
        ("Positrón","4"),
        ("Partícula Alfa","5"),
        ("Nucleo de Deuterio","6"),
    ]
    caracteristica= IntVar()
    caracteristica.set("1")
    x=2
    y=2
    z=2
    for text, mode in TIP:
        b= Radiobutton(text=text, variable=caracteristica, value=mode,font= "Cambria 12")
        b.grid(row=x,column=y)
        y=((-1)**z)+y
        if y == 2:
            x=x+1
        z=z+1
        
        
        

def botonsimulacion():
    aceptar = Button(text="Calcular", font="Cambria 10", anchor=S)
    aceptar.grid(row=10, column=1)
    #aceptar.anchor()   #aceptar.grid(row=15, column=680)  pady=10,
    

    
    