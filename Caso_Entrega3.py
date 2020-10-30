# -*- coding: utf-8 -*-
# Ecuacion del calor 1-D
from matplotlib.pylab import *
import numpy as np

L = 1
n = 100
dx = L / n

x = np.linspace(0, L, n+1)

# Arreglo con la solución
dt = 2
Nt = 50000
u = np.zeros((Nt, n+1))

K = 79.5  #
c = 450.
rho = 7800.
alpha = (K*dt)/(c*rho*(dx**2))

# Condiciones de borde
u[:,0] = 0. #izq
u[:,-1] = 20. #der 


# Condicion inicial
u[0, 1:n] = 20

for k in range(Nt-1):
    
    t = dt*k
    #print(f"k = {k}, t = {t}")
    u[k,0] = u[k,1] - 5*dx
    
    for i in range(1, n):
        u[k+1, i] =u[k,i] + alpha*(u[k,i-1] - 2*u[k,i] + u[k,i+1])

    if k % 1000 == 0:
        plot(x, u[k, :])

title("k = {}    t = {} s".format(k, k*dt))
show()




















