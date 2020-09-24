"""
María Paula Valdés
Hector Aaron Pivaral
Carné: 19146
Carne: 19640
"""

from tkinter import *
from tkinter import messagebox
import ModuloMov as graph

velocidad=0
Intensidad=0
masa=0
carga=0
angulo=0
placa=0
aceleracion=0


def particulas(m,c):
    global masa
    global carga
    masa=m
    carga=c
##velocidad, Intensidad
def validateVI_float(V,I,elevadoI, elevadoV,ang,plac):
    new_value = V.get()
    new_value2= I.get()
    ElevaI= elevadoI.get()
    ElevaV= elevadoV.get()
    Al= ang.get()
    pla= plac.get()
    try:
        new_value == float(new_value)
        ElevaV == float(ElevaV)   
        new_value2 == float(new_value2)
        ElevaI == float(ElevaI)
        Al == float(Al)
        pla == float(pla)
    except:
        messagebox.showinfo(title="Cuidado", message="Datos no válidos. Ingrese solo datos númericos.")
    global velocidad
    global Intensidad
    global angulo
    global placa
    velocidad = float(new_value)*(10**float(ElevaV))
    Intensidad= float(new_value2)*(10**float(ElevaI))
    angulo= float(Al)
    placa =float(pla)
    
def luz():
    if velocidad<=(10**8) and angulo<=360:
        return(True)
    else:
        if velocidad>=(10**8) or angulo >= 360:
            messagebox.showinfo(title="Cuidado", message="La velocidad no puede ser mayor que la velocidad luz o su angulo es mayor a 360. Revise su entrada por favor.")
        return(False)
        
    
    
def Edata(IC):
    global Intensidad
    Intensidad= IC*Intensidad
    
def graficar():
    if luz() == True:
        global aceleracion
        aceleracion=graph.aceleracionElec(masa, carga,Intensidad)
        graph.LagraFica(velocidad,aceleracion,angulo,placa)
        


    

