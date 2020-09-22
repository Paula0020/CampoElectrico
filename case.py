"""
María Paula Valdés
Hector Aaron Pivaral
Carné: 19146
Carne: 19640
"""
from tkinter import *
from tkinter import messagebox
from ERROR import *

raiz=Tk()
#raiz.config(bg=white)"
raiz.geometry("700x400")
raiz.title("Simulación de campo eléctrico 2020")
Bienvenida = Label(raiz,text= "Simulación de campo eléctrico 2020", font="Times 20")
Bienvenida.grid(row=0, column=1,columnspan=6)

carga=0
masa=0

#INTENSIDAD______________________
center = LabelFrame(raiz,bd=4,width=150, height=250,padx=3, pady=3).grid(row=1,column=1,rowspan=6)
label= Label(raiz,center,text="Intesidad de campo", font= "Cambria 12")
label.grid(row=1,column=1)
entrada= Entry(raiz,center,width=10, font= "Cambria 12")
entrada.grid(row=2,column=1)
Elevado1=Label(raiz,center,text="x10^ (N/C)", font= "Cambria 13")#Elevado
Elevado1.grid(row=3,column=1)
diez1= Entry(raiz,center,width=10, font= "Cambria 12")#texto
diez1.grid(row=4,column=1)
vertical= DoubleVar()##VALOR IMPORTANTE
vertical.set(1)    
a= Radiobutton(raiz,center,text="j",font= "Cambria 12",value=1,variable=vertical)
a.grid(row=5,column=1)
a= Radiobutton(raiz,center,text="-j",font= "Cambria 12",value=-1,variable=vertical)
a.grid(row=6,column=1)#__________________________
#VELOCIDAD________________________________________----
F = LabelFrame(raiz,bd=4,width=180, height=250,padx=3, pady=3).grid(row=1,column=3,rowspan=6)
label2= Label(raiz,F,text="Velocidad de particula", font= "Cambria 12")#magnitud
label2.grid(row=1,column=3)
entrada2= Entry(raiz,F,width=10, font= "Cambria 12")#Entrada de magnitud
entrada2.grid(row=2,column=3)
Elevado=Label(raiz,F,text="x10^ (m/s)", font= "Cambria 13")#Elevado
Elevado.grid(row=3,column=3)
diez= Entry(raiz,F,width=10, font= "Cambria 12")#texto
diez.grid(row=4,column=3)
Angle=Label(raiz,F,text="Coloque el ángulo en grados:", font= "Cambria 10")#Elevado
Angle.grid(row=5,column=3)
diez2= Entry(raiz,F,width=10, font= "Cambria 12")#texto
diez2.grid(row=6,column=3)#_________________________
##PLACA__________________________________-
placa=Label(raiz,F,text="Tamaño de placa(m):", font= "Cambria 11").grid(row=7,column=1)
long= Entry(raiz,F,width=10, font= "Cambria 12")
long.grid(row=8,column=1)#______________________________
##TIPO
label3= Label(raiz,text="Tipo de particula", font= "Cambria 15")
label3.grid(row=1, column=5, columnspan=4)
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
y=5
z=2
#nombre, masa, carga del las cantidades que estan arriba
for name, mode,extra in TIP:#es para asignar valores a los botone[command es lo que hace cuando apachas el boton]
    b= Radiobutton(raiz,text=name,font= "Cambria 12",value=mode,background="lightblue",width=15,indicator=0,variable=caracteristica,command=getchoice)
    b.grid(row=x,column=y)
    y=((-1)**z)+y#esto solo es configuracion de imagen, no afecta los valores que se tienen
    if y == 5:
        x=x+1
    z=z+1
#Funcion que define que hace el boton de terminar
def fin():
    fin= Label(raiz,text="Resultado", font= "Cambria 15")
    fin.grid(row=10, column=2, columnspan=4)
    validateVI_float(entrada2,entrada,diez1,diez,diez2,long)
    Edata(vertical.get())
    graficar()
    
aceptar = Button(raiz,text="Calcular",font="Cambria 14", command=fin)
aceptar.grid(row=7, column=5)

Salida= Button(raiz,text="Salida",bg="pink",font= "Cambria 14",command=quit)
Salida. grid(row=7, column=6)
     
raiz.mainloop()
