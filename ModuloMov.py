"""
María Paula Valdés
Hector Aaron Pivaral
Carné: 19146
Carne: 19640
"""
from vpython import *
from math import sin, cos, atan, degrees
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.pyplot import box
from numpy import rate

from vpython import *

def aceleracionElec(ParticulaMasa, carga, campo):
    acelera = (carga*campo)/ParticulaMasa
    return acelera


def LagraFica(LAVELOCIDAD, ACELERACIONELEC, ANGULOO, PLACAA):

    velocidad = LAVELOCIDAD
    aceleracionElectrica = ACELERACIONELEC
    angulo = ANGULOO
    placa = PLACAA

    def AceleracionNegativa(VELOCIDAD, ANGULO, ACELERACION, PLACA):
        velocidad = VELOCIDAD
        aceleracionElectrica = abs(ACELERACION)
        PlaacassE = PLACA
        theta = (ANGULO / 180) * np.pi
        plt.figure()
        tmax = ((2 * velocidad) * np.sin(theta)) / aceleracionElectrica
        tmaxPlacaE = (PlaacassE) / (velocidad * np.cos(theta))
        if tmax > tmaxPlacaE:
            Eltiempo = tmaxPlacaE
            printD = PlaacassE / 2
        else:
            Eltiempo = tmax
            printD = ((velocidad ** (2) * np.sin(2 * theta)) / aceleracionElectrica) / 2
        PrintiTiempo = float("{:e}".format(Eltiempo))
        Tiempo = Eltiempo * np.linspace(0, 1, 100)[:, None]

        x = ((velocidad * Tiempo) * np.cos(theta))
        y = ((velocidad * Tiempo) * np.sin(theta)) - ((0.5 * aceleracionElectrica) * (Tiempo ** 2))
        plt.xlabel("desplazamiento en el eje X (m)")
        plt.ylabel("desplazamiento en el eje y (m)")
        plt.title("Movimiento de la Particula en el Campo Electrico")
        plt.grid(b=None, which='major', axis='both')
        plt.grid(color='k', linestyle='--', linewidth=0.5)
        plt.plot(x, y, linewidth=1)
        plt.annotate("Tiempo Total = " + str(PrintiTiempo) + "seg", (printD, 0))
        plt.show()
        print(Eltiempo)

    def AceleracionPositiva(VELOCIDAD, ANGULO, ACELERACION, PLACA):
        velocidad = VELOCIDAD
        aceleracionElectrica = abs(ACELERACION)
        PlaacassE = PLACA
        theta = (ANGULO / 180) * np.pi
        plt.figure()
        tmaxPlacaE = (PlaacassE) / (velocidad * np.cos(theta))
        PrintiTiempo = float("{:e}".format(tmaxPlacaE))
        printD = PlaacassE / 2
        Tiempo = tmaxPlacaE * np.linspace(0, 1, 100)[:, None]
        x = ((velocidad * Tiempo) * np.cos(theta))
        y = ((velocidad * Tiempo) * np.sin(theta)) + ((0.5 * aceleracionElectrica) * (Tiempo ** 2))
        plt.xlabel("desplazamiento en el eje X (m)")
        plt.ylabel("desplazamiento en el eje y (m)")
        plt.title("Movimiento de la Particula en el Campo Electrico")
        plt.grid(b=None, which='major', axis='both')
        plt.grid(color='k', linestyle='--', linewidth=0.5)
        plt.plot(x, y, linewidth=1)
        plt.annotate("Tiempo Total = " + str(PrintiTiempo) + "seg", (printD, 0))
        plt.show()

    if aceleracionElectrica > 0:
        AceleracionPositiva(velocidad, angulo, aceleracionElectrica, placa)
    else:
        AceleracionNegativa(velocidad, angulo, aceleracionElectrica, placa)

#LagraFica()

