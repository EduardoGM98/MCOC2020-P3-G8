# -*- coding: utf-8 -*-
from matplotlib.pylab import *
from matplotlib.pylab import cm
import numpy as np

a = 1 #alto
b = 1 #ancho
Nx = 30 #numero de intervalos en x
Ny = 30 # numero de intervalos en y

dx = b/Nx
dy = a/Ny
# dx y dy tienen qye ser iguales!

if dx != dy:
    print("ERRORR  dx no es igual a dy")
    exit(-1)

# Funcion de conveneniencia para calcular las coordenadas del punto (i,j)
coords = lambda i,j:(dx*i,dy*j)
x,y = coords(4,2)


def imshowbien(u):
	imshow(u.T[Nx::-1,:],cmap=cm.coolwarm, interpolation="bilinear")
	cbar=colorbar(extend='both', cmap=cm.coolwarm)
	ticks = arange(0,35,5)
	ticks_Text=["{}".format(deg) for deg in ticks]
	cbar.set_ticks(ticks)
	cbar.set_ticklabels(ticks_Text)
	clim(0,30)

	xlabel('b')
	ylabel('a')
	xTicks_N = arange(0,Nx+1,3)
	yTicks_N = arange(0,Ny+1,3)
	xTicks = [coords(i,0)[0] for i in xTicks_N]
	yTicks = [coords(0,i)[1] for i in yTicks_N]
	xTicks_Text=["{0:.2f}".format(tick) for tick in xTicks]
	yTicks_Text=["{0:.2f}".format(tick) for tick in yTicks]

	xticks(xTicks_N, xTicks_Text, rotation='vertical')
	yticks(yTicks_N, yTicks_Text)
	margins(0.2)
	subplots_adjust(bottom=0.15) 


u_k = zeros((Nx+1, Ny+1), dtype=double)
u_km1 = zeros((Nx+1, Ny+1), dtype=double)

# Condicion de borde inicial
u_k[:,:] = 20 #en todas las celdas

#Parametros
dt = 0.01    # s
K = 79.5     # m^2/s
c = 450      # J/Kg*C
rho = 7800   # Kg/m^3

alpha = (K*dt)/(c*rho*(dx**2))

# Loop en el tiempo
minuto = 60
hora = 60*minuto
dia = 24*hora

dt = 1*minuto
dnext_t = 0.5*hora

next_t = 0
framenum = 0

T = 1*dia
Days = 4*T # Cuantos dias quiero simunlar

#vectores para acumular la temperatura en puntos interesantes
u_0=zeros(int32(Days/dt))
u_P1=zeros(int32(Days/dt))
u_P2=zeros(int32(Days/dt))
u_P3=zeros(int32(Days/dt))


def truncate(n, decimals=0):
    multiplier = 10**decimals
    return int(n*multiplier)/multiplier

# Loops en el tiempo
for k in range(int32(Days/dt)):
    t =dt*(k+1)
    dias = truncate(t/dia,0)
    horas = truncate((t-dias*dia)/hora,0)
    minutos = truncate((t-dias*dia - horas*hora)/minuto,0)-1
    titulo = "k = {0:05.0f}".format(k) + " t = {0:02.0f}d {1:02.0f}h {2:02.0f}m ".format(dias,horas,minutos)
    
    # CB esenciales, se repiten en cada iteracion
    u_ambiente= 20 + 10*sin((2*pi/T)*t)
    u_k[0, :] = u_k[1, :] -0*dx               #izq, gradiente 0
    u_k[:, 0] = u_k[:, 1] -0*dy               #inf, gradiente 0
    u_k[:, -1] = u_ambiente                    #sup
    u_k[-1, :] = u_k[-2, :] -0*dx              #der, gradiente 0  
    # (f(x+h) - f(x))/dx = algo
    
    for i in range (1,Nx):
        for j in range(1,Ny):
            
            #Algoritmo de diferencias finitas para 2-D
            #Laplaciano
            nabla_u_k = (u_k[i-1,j] + u_k[i+1,j] + u_k[i,j-1] + u_k[i,j+1] -4*u_k[i,j]) /dx**2
            
            #Forward Euler
            u_km1[i,j] = u_k[i,j] + alpha*nabla_u_k
    # Avanzar la solucion a k+1
    u_k = u_km1
    
    # CB denuevo, porsia
    u_k[0, :] = u_k[1, :] -0*dx               #izq, gradiente 0
    u_k[:, 0] = u_k[:, 1] -0*dy               #inf, gradiente 0
    u_k[:, -1] = u_ambiente                    #sup
    u_k[-1, :] = u_k[-2, :] -0*dx                     # der
    # (f(x+h) - f(x))/dx = algo
    u_0[k]=u_k[int(Nx/2), -1]
    u_P1[k]=u_k[int(Nx/2), int(Ny/2)]
    u_P2[k]=u_k[int(Nx/2), int(3*Ny/4)]
    u_P3[k]=u_k[int(3*Nx/4), int(3*Ny/4)]
    
    
    #Grafico en d_next
    if t>next_t:
        figure(1)
        imshowbien (u_k)
        title(titulo)
        savefig("Caso_7_img/frame_{0:04.0f}.png".format(framenum))
        framenum +=1
        next_t += dnext_t
        close(1)

figure(2)
plot(range(int32(Days/dt)), u_0, linestyle= ":",  color="black", label="Ambiente")
plot(range(int32(Days/dt)), u_P1, label="P1")
plot(range(int32(Days/dt)), u_P2, label="P2")
plot(range(int32(Days/dt)), u_P3, label="P3")
title("Evolucion de temperatura en puntos")
legend()


show()
