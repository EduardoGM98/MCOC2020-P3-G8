# -*- coding: utf-8 -*-
# Ecuacion del calor 1-D
from matplotlib.pylab import *
import math


def graficarMallas(dt):
    deltaT = 10
    tu = arange(0,90000, deltaT)
    L = 1.04
    n = 20
    dx = L / n

    x = linspace(0, L, n+1)


    # Arreglo con la solución
    Nt = len(tu)
    u = zeros((Nt, len(tu)))

    K = 0.001495  #
    c = 1.023
    rho = 2476
    alpha = (K*dt)/(c*rho*(dx**2))
    
    # Condiciones de borde
    u[:,0] = 0. #izq
    u[:,-1] = 0. #der 


    # Condicion inicial
    u[0, 1:n] = 20


    for k in range(Nt-1):
    
        t = dt*k
        for i in range(1, n):
            u[k+1, i] =u[k,i] + alpha*(u[k,i-1] - 2*u[k,i] + u[k,i+1])

        #if k % 200 == 0:
            #   plot(x, u[k, :])

    plot(tu, u[:,1])

graficarMallas(1)
graficarMallas(5)
graficarMallas(10)
graficarMallas(50)
graficarMallas(100)

trickx = [0, 5*60*60, 10*60*60, 15*60*60, 20*60*60, 25*60*60]
trickx_txt = ['0', '5', '10', '15', '20', '25']
xticks(trickx, trickx_txt) 

legend(('Malla 20 delta_t = 1', 'Malla 20 delta_t = 5','Malla 20 delta_t = 10', 'Malla 20 delta_t = 50', 'Malla 20 delta_t = 100'),prop = {'size': 10}, loc='upper right')
grid()
title("x = 0.104 m ")
plt.ylabel('Temperatura [C°]')
plt.xlabel('Tiempo [horas] ')
show()



