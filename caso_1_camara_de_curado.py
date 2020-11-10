  # -*- coding: utf-8 -*-
from matplotlib.pylab import *
from matplotlib.pylab import cm
import numpy as np
from calor_de_hidratacion import Calor_de_hidratacion

a = 0.5 #alto   50 cm
b = 0.54 #ancho 54 cm
c = 1.04 #largo 104 cm

Nx = 20 # numero de intervalos en x  
Ny = 20 # numero de intervalos en y   
Nz = 20 # numero de intervalos en z  

dx = b/Nx  
dy = a/Ny
dz = c/Nz


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
    clim(0,40)

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


u_k = u_k = zeros((Nz+1, Nx+1, Ny+1), dtype=double)
u_km1 = u_k = zeros((Nz+1, Nx+1, Ny+1), dtype=double)

# Condicion de borde inicial
u_k[:,:] = 20 #en todas las celdas

#Parametros
dt = 0.01    # s
K = 79.5     # m^2/s
c = 450      # J/Kg*C
rho = 7800   # Kg/m^3

alphaX = (K*dt)/(c*rho*(dx**2))
alphaY = (K*dt)/(c*rho*(dy**2))
alphaZ = (K*dt)/(c*rho*(dz**2))


# Loop en el tiempo
minuto = 60
hora = 60*minuto
dia = 24*hora

dt = 1*minuto
dnext_t = 0.5*hora

next_t = 0
framenum = 0

T = 1*dia
Days = 2*T # Cuantos dias quiero simunlar

#vectores para acumular la temperatura en puntos interesantes
u_P1=zeros(int32(Days/dt))
u_P2=zeros(int32(Days/dt))
u_P3=zeros(int32(Days/dt))
u_P4=zeros(int32(Days/dt))
u_P5=zeros(int32(Days/dt))
u_P6=zeros(int32(Days/dt))
u_P7=zeros(int32(Days/dt))
u_P8=zeros(int32(Days/dt))
u_P9=zeros(int32(Days/dt))
u_P10=zeros(int32(Days/dt))
u_P11=zeros(int32(Days/dt))
u_P12=zeros(int32(Days/dt))
u_P13=zeros(int32(Days/dt))
u_P14=zeros(int32(Days/dt))
u_P15=zeros(int32(Days/dt))



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
      
    u_k[:, -1, :] = u_k[:, -2, :]                       # borde inf, gradiente 0                   
    u_k[:, 0, :] = 20 + 10*sin((2*pi/T)*t)              # borde sup, temperatura ambiente variaa

    u_k[-1, :, :] =  u_k[-2, :, :]                       # borde de atras 
    u_k[0, :, :] = u_k[1, :, :]                       # borde de adelante 

    u_k[:, :, 0] =  u_k[:, :, 1]                       # borde de izq 
    u_k[:, :, -1] = u_k[:, :, -2]                       # borde de der
    
    # (f(x+h) - f(x))/dx = algo
    for z in range (1,Nz):
        for i in range (1,Nx):
            for j in range(1,Ny):
            
                #Algoritmo de diferencias finitas para 3-D
                #Laplaciano
                nabla_u_kX = u_k[z,i-1,j] + u_k[z,i+1,j] 
                nabla_u_kY = u_k[z,i,j-1] + u_k[z,i,j+1] 
                nabla_u_kZ = u_k[z+1,i,j] + u_k[z-1,i,j] 
                #Forward Euler
                u_km1[z,i,j] = u_k[z,i,j] + alphaX*nabla_u_kX + alphaY*nabla_u_kY + alphaZ*nabla_u_kZ + Calor_de_hidratacion(t)*dt
                # Avanzar la solucion a k+1
                u_k = u_km1
    
    # CB denuevo, porsia
    u_k[:, -1, :] = u_k[:, -2, :]                       # borde inf, gradiente 0                   
    u_k[:, 0, :] = 20 + 10*sin((2*pi/T)*t)              # borde sup, temperatura ambiente variaa

    u_k[-1, :, :] =  u_k[-2, :, :]                       # borde de atras 
    u_k[0, :, :] = u_k[1, :, :]                       # borde de adelante 

    u_k[:, :, 0] =  u_k[:, :, 1]                       # borde de izq 
    u_k[:, :, -1] = u_k[:, :, -2]                       # borde de der
    # (f(x+h) - f(x))/dx = algo
    
    u_P1[k]=u_k[10, 10, 10]
    
    """
    u_P1[k]=u_k[15, 9, 11] 
    u_P2[k]=u_k[10, 9, 11]
    u_P3[k]=u_k[10, 9, 20]
    u_P4[k]=u_k[10, 17, 11]
    u_P5[k]=u_k[1, 9, 11]
    u_P6[k]=u_k[10, 9, 3]
    u_P7[k]=u_k[10, 13, 11]
    u_P8[k]=u_k[1, 5, 11]
    u_P9[k]=u_k[10, 9, 6]
    u_P10[k]=u_k[19, 9, 11]
    u_P11[k]=u_k[10, 31 11]
    u_P12[k]=u_k[5, 9, 1]
    #u_P13[k]=ambiente
    u_P14[k]=u_k[10, 9, 16]
    #u_P15[k]=probeta
    """   
    
    
    #Grafico en d_next
    if t>next_t:
        figure(1)
        imshowbien (u_k[10])
        title(titulo)
        savefig("Ejemplo/frame_{0:04.0f}.png".format(framenum))
        framenum +=1
        next_t += dnext_t
        close(1)

figure(2)

plot(range(int32(Days/dt)), u_P1, label="Sensor1")
"""
plot(range(int32(Days/dt)), u_P1, label="Sensor1")
plot(range(int32(Days/dt)), u_P1, label="Sensor1")
plot(range(int32(Days/dt)), u_P2, label="Sensor2")
plot(range(int32(Days/dt)), u_P3, label="Sensor3")
plot(range(int32(Days/dt)), u_P4, label="Sensor4")
plot(range(int32(Days/dt)), u_P5, label="Sensor5")
plot(range(int32(Days/dt)), u_P6, label="Sensor6")
plot(range(int32(Days/dt)), u_P7, label="Sensor7")
plot(range(int32(Days/dt)), u_P8, label="Sensor8")
plot(range(int32(Days/dt)), u_P9, label="Sensor9")
plot(range(int32(Days/dt)), u_P10, label="Sensor10")
plot(range(int32(Days/dt)), u_P11, label="Sensor11")
plot(range(int32(Days/dt)), u_P12, label="Sensor12")
#plot(range(int32(Days/dt)), u_P13, label="Sensor13")
plot(range(int32(Days/dt)), u_P14, label="Sensor14")
#plot(range(int32(Days/dt)), u_P15, label="Sensor15")
"""
title("Evolucion de temperatura camara de curado")
legend()

savefig("ejem_grupo8.png")
show()
