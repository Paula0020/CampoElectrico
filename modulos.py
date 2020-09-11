"""
María Paula Valdés
Hector Aaron Pivaral
Carné: 19146
Carne:
"""
import tkinter as tk
from tkinter import *

carga=0
masa=0


# Label es lo que se muestra en pantalla,(texto) y donde dice Entry es para el input
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
        ("Proton",1.673E-27,1.6E-19),
        ("Electron",9.11E-31,-1.6E-19),
        ("Neutron",1.675E-27,0),
        ("Partícula Alfa",6.64E-27,3.2E-19),
        ("Núcleo de Deuterio",3.34E-27,1.602E-19),
        ("Tau", 3.16E-27,-1.6E-19),
        ("Núcleo de Tritio",5.027E-27,1.6E-19),
        ("Positron",9.1E-31,1.6E-19),
    ]
    
    caracteristica= DoubleVar()
    caracteristica.set(1)
    def record():# este metodo es para obtener el tercer valor de la lista(que en realidad seria la masa de la particula)
        for t,m,y in TIP:
            if m == caracteristica.get():
                return(y)
            
    
    #Esto solo es para mostrar que si me quedó () 
    def getchoice():
        carga= str(record())
        masa= str(caracteristica.get())
        print("Su carga es : "+carga)
        print("Su masa es : "+ masa)
        
    x=2
    y=2
    z=2
    for name, mode,extra in TIP:#es para asignar valores a los botone[command es lo que hace cuando apachas el boton]
        b= Radiobutton(text=name,font= "Cambria 12",value=mode,selectcolor="lightblue",variable=caracteristica,command=getchoice)
        b.grid(row=x,column=y)
        y=((-1)**z)+y#esto solo es configuracion de imagen, no afecta los valores que se tienen
        if y == 2:
            x=x+1
        z=z+1
def fin():
    fin= tk.Label(text="Resultado", font= "Cambria 15")
    fin.grid(row=10, column=2, columnspan=4)
    
def botonsimulacion():
    aceptar = Button(text="Calcular", font="Cambria 10", anchor=S, command=fin)
    aceptar.grid(row=7, column=1)
    
    

    
    