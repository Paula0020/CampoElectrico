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


    initialHeight = 0.25
    initialVelocity = 10#Parametrrooooooooooooooooooooooooooooooooooooooooo
    Angle = 0.5#Parametrrooooooooooooooooooooooooooooooooooooooooo

    # Set up the display window

    g.background = color.white
    g.title = 'Projectile Motion'
    g.x = 0
    g.y = 0
    g.width = 1000
    g.height = 800
    g.range = 1
    g.center = vec(1, initialHeight, 0)

    # Creating obects

    table = box(pos=vec(-1, initialHeight - 0.01, 0), size=vec(2,
                                                                     0.01, 1), color=color.cyan)

    ball = sphere(pos=vec(0, initialHeight, 0), radius=0.02,
                  color=color.green, make_trail=True)

    floor = box(pos=vec(0, 0, 0), size=vec(5, 0.01, 1),
                color=color.red)

    label1 = label4(pos=vec(1, 0.7, 0), text='Current velocity vx: ')
    label2 = label4(pos=vec(1, 0.6, 0), text='Current velocity vy: ')
    label3 = label4(pos=vec(1, -0.4, 0), text='Distance: ')
    label4 = label4(pos=vec(1, -0.6, 0), text='Time: ')
    label5 = label4(pos=vec(1, -0.5, 0), text='Angle: ')

    # Paramaters

    t = 0
    dt = 0.001
    g = -9.8  # m/s^2#Parametrrooooooooooooooooooooooooooooooooooooooooo
    gravity = vec(0, g * dt, 0)

    # Velocity vector for ball:

    ballv = vec(initialVelocity * cos(Angle * pi / 180), initialVelocity
                   * sin(Angle * pi / 180), 0)

    # Simulate event

    while True:
        rate(300)
        ballv = ballv + gravity
        ball.pos += ballv * dt
        velocity = str(ballv)
        position = str(ball.pos)
        y = (position.split(',')[1])[1:-1]
        vx = (velocity.split(',')[0])[1:-1]
        vy = (velocity.split(',')[1])[1:-1]
        label1.text = 'Current velocity vx: ' + vx + ' m/s'
        label2.text = 'Current velocity vy: ' + vy + ' m/s'

        # breaks loop when ball hits the ground

        if float(y) <= 0:
            angle = degrees(atan(abs(float(vy) / float(vx))))
            t = format(t, '.3f')
            angle = format(angle, '.3f')
            label3.text = 'Distance: ' + (position.split(',')[0])[1:-1] \
                          + ' meter'
            label4.text = 'Time: ' + t + ' sec'
            label5.text = 'Angle: ' + angle + ' degrees'

            print('Position x =', position.split(',')[0], 'meter, time ='
                  , t, 's')

            print('Angle at impact:', angle)
            break

        t += dt

LagraFica()
