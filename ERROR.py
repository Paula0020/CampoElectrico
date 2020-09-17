"""
María Paula Valdés
Hector Aaron Pivaral
Carné: 19146
Carne: 19640
"""

from tkinter import *
from tkinter import messagebox


velocidad=0
Intensidad=0
masa=0
carga=0
angulo=0
verticalI=0

def particulas(m,c):
    print(str(m))
    print(str(c))
    m= masa
    c=carga
##velocidad, Intensidad
def validateVI_float(V,I,elevadoI, elevadoV,ang):
    new_value = V.get()
    new_value2= I.get()
    ElevaI= elevadoI.get()
    ElevaV= elevadoV.get()
    Al= ang.get()
    try:
        new_value == float(new_value)
        ElevaV == float(ElevaV)
        velocidad = float(new_value)*(10**float(ElevaV))
        new_value2== float(new_value2)
        ElevaI == float(ElevaI)
        Intensidad= float(new_value2)*(10**float(ElevaI))
        Al == float(Al)
        angulo= float(Al)
        print(str(velocidad)+"\n"+str(Intensidad)+"\n"+str(angulo))
    except:
        messagebox.showinfo(title="Cuidado", message="Datos no válidos")

def Edata(IC):
    verticalI=IC
    

