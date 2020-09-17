"""
María Paula Valdés
Hector Aaron Pivaral
Carné: 19146
Carne: 19640
"""
import tkinter as tk
from tkinter import *
from ERROR import *

carga=0
masa=0


#INTENSIDAD
label= tk.Label(text="Intesidad de campo", font= "Cambria 13")
label.grid(row=1,column=0)
entrada= tk.Entry(width=10, font= "Cambria 12")
entrada.grid(row=2,column=0)

vertical= DoubleVar()
vertical.set(1)    
a= Radiobutton(text="j",font= "Cambria 12",value=1,variable=vertical)
a.grid(row=3,column=0)
a= Radiobutton(text="-j",font= "Cambria 12",value=-1,variable=vertical)
a.grid(row=4,column=0)
#VELOCIDAD
    
label2= tk.Label(text="Velocidad de particula", font= "Cambria 13")
label2.grid(row=1,column=1)
entrada2= tk.Entry(width=10, font= "Cambria 12")
entrada2.grid(row=2,column=1)
##TIPO
label3= tk.Label(text="Tipo de particula", font= "Cambria 15")
label3.grid(row=1, column=2, columnspan=4)
     # electrón, positrón, protón, neutrón, partícula alfa, núcleo de deuterio, muón
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
    
def getchoice():
    for t,m,y in TIP:
        if m == caracteristica.get():
            particulas(caracteristica.get(),y)
            
x=2
y=2
z=2
for name, mode,extra in TIP:#es para asignar valores a los botone[command es lo que hace cuando apachas el boton]
    b= Radiobutton(text=name,font= "Cambria 12",value=mode,background="lightblue",indicator=0, width=15,variable=caracteristica,command=getchoice)
    b.grid(row=x,column=y)
    y=((-1)**z)+y#esto solo es configuracion de imagen, no afecta los valores que se tienen
    if y == 2:
        x=x+1
    z=z+1
    
def fin():
    fin= tk.Label(text="Resultado", font= "Cambria 15")
    fin.grid(row=10, column=2, columnspan=4)
    validateV_float(entrada2)
    validateI_float(entrada)
    print("Resultado")
    

aceptar = Button(text="Calcular",font="Cambria 10", anchor=S, command=fin)
aceptar.grid(row=7, column=1)
    
    

    
    

    
    