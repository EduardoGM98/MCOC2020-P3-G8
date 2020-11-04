from matplotlib.pylab import *
from matplotlib import cm

a=1 #alto del dominio
b=1 #ancho del dominio 
Nx=30 #Numero de intervalos en x
Ny=30 ##Numero de intervalos en y

dx=b/Nx #discretizacion espacios en x
dy=a/Ny #discretizacion espacios en y

h=dx

if dx != dy:
    print("ERROR!!!!! dx != dy")
    exit(-1) # -1 le dice al SO que el programa falla....
    
# Funcion de conveneniencia para calcular las coordenadas del punt(1,1)
def coords(i,j): return (dx*i, dy*j)

x,y=coords(4,2)

print("x: ", x)
print("y: ", y)

def imshowbien(u):
    imshow(u.T[Nx::-1,:],cmap=cm.coolwarm, interpolation="bilinear")
    cbar=colorbar(extend="both", cmap=cm.coolwarm)
    ticks=arange(0,35,5)
    ticks_Text=["{}".format(deg) for deg in ticks]
    cbar.set_ticks(ticks)
    cbar.set_ticklabels(ticks_Text)
    clim(0, 30)
    
    xlabel("b")
    ylabel("a")
    xTicks_N=arange(0, Nx+1,3)
    yTicks_N=arange(0, Ny+1,3)
    xTicks=[coords(i,0)[0] for i in xTicks_N]
    yTicks=[coords(i,0)[0] for i in yTicks_N]
    xTicks_Text=["{0:.2f}".format(tick) for tick in xTicks]
    yTicks_Text=["{0:.2f}".format(tick) for tick in yTicks]
    xticks(xTicks_N,xTicks_Text,rotation="vertical")
    yticks(yTicks_N,yTicks_Text)
    margins(0,1)
    subplots_adjust(bottom=0.15)
    
    
u_k = zeros((Nx+1,Ny+1),dtype=double) #dtyoe es el tipo de dato
u_km1 = zeros((Nx+1,Ny+1),dtype=double) #dtyoe es el tipo de dato

#Condicion de borde inicial
u_k[:,:]=20 #20 grados inicial en todas partes

#Parametros problema (hierro)
dt=0.01
K=79.5
c=450
rho=7800
alfa=K*dt/(c*rho*dx**2)

print(f"dt={dt}")
print(f"dx={dx}")
print(f"K={K}")
print(f"c={c}")
print(f"rho={rho}")
print(f"alfa={alfa}")

#loop en el tiempo
minuto=60
hora=3600
dia=24*3600

dt=1*minuto
dnext_t=0.5*hora

next_t=0
framenum=0

T=1*dia
Days=1*T #cuantos dias quiero ssimular

#vectores para acumular la temperatura en puntos interesantes
u_P1=zeros(int32(Days/dt))
u_P2=zeros(int32(Days/dt))
u_P3=zeros(int32(Days/dt))

def truncate(n, decimals=0):
    multiplier=10**decimals
    return int(n*multiplier)/multiplier

#loop en el tiempo
for k in range(int32(Days/dt)):
    t=dt*(k+1)
    dias=truncate(t/dia,0)
    horas=truncate((t-dias*dia)/hora,0)
    minutos=truncate((t-dias*dia-horas*hora)/minuto,0)
    titulo="K={0:05.0f}".format(k)+"t={0:02.0f}d {1:02.0f}h {2:02.0f}m ".format(dias, horas, minutos)
    print(titulo)
    
    # CB esenciales, se repiten en cada iteración
    u_k[0,:] = 20 #Borde izq
    u_k[:,0] = 20 #Borde inferior
    u_k[:,-1] = 0     #u_k[:,-2] - 0*dy  #Gradiente 0, borde superior
    
    #(f(x+dx)-f(x))/dx=algo
    u_k[-1,:]=0        #u_k[-2,:]-10*dx #Borde derecho, gradiente -10
    
    for i in range(1, Nx):
        for j in range(1,Ny):
            
            # Algoritmo de diferencias finitas 2-D para difusion
            # Laplaciano
            
            nabla_u_k=(u_k[i-1,j] + u_k[i+1,j] + u_k[i,j-1] + u_k[i,j+1] -4*u_k[i,j])/h**2
            
            #Forware Euler
            u_km1[i,j]=u_k[i,j]+alfa*nabla_u_k
            
    #Avanzar la solucion a k+1
    u_k=u_km1
    
    #CB de nuevo, para asegurar cumplimiento
    u_k[0,:] = 20 #Borde izq
    u_k[:,0] = 20 #Borde inferior
    u_k[:,-1] = 0  #u_k[:,-2]- 0*dy  #Gradiente 0, borde superior
    
    #(f(x+dx)-f(x))/dx=algo
    u_k[-1,:]= 0   #u_k[-2,:]-10*dx #Borde derecho, gradiente -10
    
    #Encuentro temperaturas en puntos interesantes
    u_P1[k]=u_k[int(Nx/2), int(Ny/2)]
    u_P2[k]=u_k[int(Nx/2), int(3*Ny/4)]
    u_P3[k]=u_k[int(3*Nx/4), int(3*Ny/4)]
    
    
    #grafico en dnext_t
    if t>next_t:
        figure(1)
        imshowbien(u_k)
        title(titulo)
        savefig("Caso_1_img/frame_{0:04.0f}.png".format(framenum))
        framenum +=1
        next_t += dnext_t
        close(1)
        
#Plote historia de temperaturas en puntos interesantes
figure(2)
plot(range(int32(Days/dt)), u_P1, label="P1")
plot(range(int32(Days/dt)), u_P2, label="P2")
plot(range(int32(Days/dt)), u_P3, label="P3")
title("Evolucion de temperatura en puntos")
legend()
show()