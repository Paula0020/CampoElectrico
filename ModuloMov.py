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

def LaAnimacion(ACELERACIONELECTRICA, VELCOIDAD, ANGULO):
    scene = canvas(title='Charged Particle in Electric Field', width=1000, height=800, center=vector(0, 0, 0),
                    align="left",
                    background=vector(1, 1, 1))

    i = 1
    AceleracionElectrica = -ACELERACIONELECTRICA  # 9.8  # Aqui cabal se pone el valor de la aceleracion
    initialVelocity = VELCOIDAD  # 12# Aqui cabal se pone el valor de la rapidez
    Angle = ANGULO  # Aqui cabal se pone el valor del angulo
    ParaElDefACE = abs(AceleracionElectrica)
    ParaElDefVeloc = abs(initialVelocity)
    ElDefDefinitivo = ParaElDefVeloc-ParaElDefACE
    ElquesiEs = abs(ElDefDefinitivo)
    if ElquesiEs > 1.0E13:
        dt = 0.000000000001
    elif ElquesiEs >10.0E11:
        dt = 0.0000000000001
    elif ElquesiEs > 1.0E10:
        dt = 0.0000001
    else:
        dt = 0.000000001
    # TamañoDePlaca = 50  # Aqui cabala se pone el valor que el usuario ingreso
    # TamañoDePlacaE = box(pos=vector(TamañoDePlaca / 2, 0, 0), size=vector(TamañoDePlaca, 0.10, 0), color=color.blue)

    particle = sphere(pos=vector(0, 0, 0), radius=0.00000002, color=color.blue, make_trail=True)
    # label1 = label(pos=vec(1, 0.7, 0), text='Current velocity vx: ')
    # label2 = label(pos=vec(1, 0.6, 0), text='Current velocity vy: ')
    label3 = label(pos=vec(0, 0, 0), text='Distance: ')
    label4 = label(pos=vec(0, (initialVelocity ** (2) * sin(Angle * pi / 180) ** (2)) / (2 * abs(AceleracionElectrica)), 0),text='Altura Maxima: ')
    # label4 = label(pos=vec(1, -0.6, 0), text='Time: ')
    # label5 = label(pos=vec(1, -0.5, 0), text='Angle: ')

    t = 0
    #dt = 0.0000000000001#0.000000001
    i +=1
    #El 0.0000000000001
    gravity = vector(0, AceleracionElectrica * dt, 0)
    Particlev = vector(initialVelocity * cos(Angle * pi / 180), initialVelocity
                       * sin(Angle * pi / 180), 0)
    MaximumHeight = (initialVelocity ** (2) * sin(Angle * pi / 180) ** (2)) / (2 * abs(AceleracionElectrica))
    ElVerdaderoMaximumHeight = float("{:.6f}".format(MaximumHeight))

    while True:
        rate(300)
        Particlev = Particlev + gravity
        particle.pos += Particlev * dt
        velocity = str(Particlev)
        position = str(particle.pos)
        y = (position.split(',')[1])[1:-1]
        vx = (velocity.split(',')[0])[1:-1]
        vy = (velocity.split(',')[1])[1:-1]

        if float(y) <= 0:
            angle = degrees(atan(abs(float(vy) / float(vx))))
            t = format(t, '.3f')
            angle = format(angle, '.3f')

            print('Position x =', position.split(',')[0], 'meter, time ='
                  , t, 's')

            label3.text = 'Distance: ' + (position.split(',')[0])[1:-1] \
                          + ' meter'
            label4.text = 'Altura Maxima: ' + str(ElVerdaderoMaximumHeight) + ' meter'


            print('Angle at impact:', angle)
            break
    t += dt

def LagraFica(ACELERACIONELECTRICA, VELCOIDAD, ANGULO):
    velocidad = VELCOIDAD
    aceleracionElectrica = ACELERACIONELECTRICA

    theta = (ANGULO / 180) * np.pi
    plt.figure()

    tmax = ((2 * velocidad) * np.sin(theta)) / abs(aceleracionElectrica)#valor abs porque el tiempo siempre es+
    Tiempo = tmax * np.linspace(0, 1, 100)[:, None]
    x = ((velocidad * Tiempo) * np.cos(theta))
    y = ((velocidad * Tiempo) * np.sin(theta)) + ((0.5 * aceleracionElectrica) * (Tiempo ** 2))

    plt.plot(x, y)  # plot each dataset: columns of x and columns of y
    # plt.ylim([0,35])
    plt.show()
    print(tmax)


#LagraFica()

