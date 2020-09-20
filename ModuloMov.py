"""
María Paula Valdés
Hector Aaron Pivaral
Carné: 19146
Carne: 19640
"""
from vpython import *
from math import sin, cos, atan, degrees

from matplotlib.pyplot import box
from numpy import rate

from vpython import *

def aceleracionElec(ParticulaMasa, carga, campo):
    acelera = (carga*campo)/ParticulaMasa
    return acelera

def LagraFica():
    
    scene2 = canvas(title='Charged Particle in Electric Field', width=1000, height=800, center=vector(0, 0, 0),
                    align="left",
                    background=vector(1, 1, 1))
    Grafica1 = graph(width=800, height=400, align="left", title='Movimiento de la Particula', xtitle='Eje X (m)',
                     ytitle='Eje y (m)', foreground=color.black, background=color.white)

    Graph_MovElec = gcurve(graph=Grafica1, color=color.blue)

    AceleracionElectrica = -98000000000000  # Aqui cabal se pone el valor de la aceleracion
    initialVelocity = 500000000  # Aqui cabal se pone el valor de la rapidez
    Angle = 50  # Aqui cabal se pone el valor del angulo
    # TamañoDePlaca = 50  # Aqui cabala se pone el valor que el usuario ingreso
    # TamañoDePlacaE = box(pos=vector(TamañoDePlaca / 2, 0, 0), size=vector(TamañoDePlaca, 0.10, 0), color=color.blue)

    particle = sphere(pos=vector(0, 0, 0), radius=0.02, color=color.blue, make_trail=True)
    # label1 = label(pos=vec(1, 0.7, 0), text='Current velocity vx: ')
    # label2 = label(pos=vec(1, 0.6, 0), text='Current velocity vy: ')
    label3 = label(pos=vec(1, -0.4, 0), text='Distance: ')
    # label4 = label(pos=vec(1, -0.6, 0), text='Time: ')
    # label5 = label(pos=vec(1, -0.5, 0), text='Angle: ')

    t = 0
    dt = 0.00000002

    gravity = vector(0, AceleracionElectrica * dt, 0)
    Particlev = vector(initialVelocity * cos(Angle * pi / 180), initialVelocity
                       * sin(Angle * pi / 180), 0)
    xxx = 0
    yyy = 0
    while True:
        rate(300)
        Particlev = Particlev + gravity
        particle.pos += Particlev * dt
        velocity = str(Particlev)
        position = str(particle.pos)
        x = (position.split(',')[0])[1:-1]
        y = (position.split(',')[1])[1:-1]
        vx = (velocity.split(',')[0])[1:-1]
        vy = (velocity.split(',')[1])[1:-1]
        Graph_MovElec.plot(pos=(float(x), float(y)))

        # breaks loop when ball hits the ground

        if float(y) <= 0:
            angle = degrees(atan(abs(float(vy) / float(vx))))
            t = format(t, '.3f')
            angle = format(angle, '.3f')

            print('Position x =', position.split(',')[0], 'meter, time ='
                  , t, 's')

            label3.text = 'Distance: ' + (position.split(',')[0])[1:-1] \
                          + ' meter'

            print('Angle at impact:', angle)
            break
    t += dt


#LagraFica()

LagraFica()
