# MCOC2020-P3-G8
# Entrega 3


![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Imagen_Memoria_1.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Imagen_Memoria_2.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Imagen_Memoria_3.png)<br>

Grafico de 5000 pasos

![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Grafico_5000_pasos.png)

Grafico de 25000 pasos

![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Grafico_25000_pasos.png)

Grafico de 50000 pasos

![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Grafico_50000_pasos.png)<br>


Como se puede observar en los gráficos todas las mallas convergen a 20 °C. También es rescatable mencionar que a medida que aumentaba el paso la linea correspondiente a ese aumento de paso se va enderzando con respecto a la anterior, hasta llegar a el ultimo paso donde el ultimo paso correspondo a una linea practicamente recta. 

¿En que casos cree que se podria utilizar una condicion de borde natural?

Creemos que esto podria ocurrir cuando falta una condicion de borde, las que dejan "espacios" en blanco, de tal manera que con una de borde natural se completan los espacios.


# Entrega 5

- Descripción de como hay que cambiar las condiciones de borde, en el código.
  - R. Si la condición de borde es simplemente una temperatura, se debe ingresar el valor de esa temperatura en el borde correspondiente de la condición. En el caso de que sea un gradiente, lo que hay que hacer es que el borde del punto que se quiera calcular sea igual al mismo borde del punto anterior menos el valor del gradiente por el diferencial de x. Esto es siguiendo la lógica de (f(x+h)-f(x))/dx=algo, lo que en términos de código se expresa de la forma u_k[-1, :] = u_k[-2, :] - 0*dx para el gradiente en el borde derecho con valor 0. Finalmente, si la condición de borde es la temperatura ambiental, esta se comporta como una sinusoide que varia en X grados de temperatura en un periodo de tiempo T, por lo que matemáticamente se expresa como X*sin((2*pi/T)*t). A esto habría que sumarle la temperatura inicial del medio ambiente.

*Para realizar los graficos se utilizaron los puntos mencionados en el enunciado, P1(a/2, b/2), P2 (a/2, 3b/4), P3 (3a/4, 3b/4)*

- Caso 1


![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso1.png)

Imagenes caso 1 a las 0, 2, 6, 12 y 24 horas:

![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_1_0h.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_1_2h.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_1_6h.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_1_12h.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_1_24h.png)

gif:

![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Gif1.gif)



- Caso 2


![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso2.png)

Imagenes caso 2 a las 0, 2, 6, 12 y 24 horas:

![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_2_0h.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_2_2h.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_2_6h.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_2_12h.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_2_24h.png)

gif:

![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Gif2.gif)


- Caso 3


![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso3.png)

Imagenes caso 3 a las 0, 2, 6, 12 y 24 horas:

![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_3_0h.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_3_2h.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_3_6h.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_3_12h.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_3_24h.png)

gif:

![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Gif3.gif)


- Caso 4


![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso4.png)

Imagenes caso 4 a las 0, 2, 6, 12 y 24 horas:

![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_4_0h.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_4_2h.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_4_6h.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_4_12h.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_4_24h.png)

gif:

![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Gif4.gif)


- Caso 5


![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso5.png)

Imagenes caso 5 a las 0, 2, 6, 12 y 24 horas:

![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_5_0h.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_5_2h.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_5_6h.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_5_12h.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_5_24h.png)

gif:

![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Gif5.gif)


- Caso 6


![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso6.png)

Imagenes caso 6 a las 0, 2, 6, 12 y 24 horas:

![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_6_0h.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_6_2h.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_6_6h.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_6_12h.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_6_24h.png)

gif:

![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Gif6.gif)


- Caso 7

![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso7.png)

Imagenes caso 6 a las 0, 2, 6, 12 y 24 horas:

![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_7_0h.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_7_2h.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_7_6h.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_7_12h.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Caso_7_24h.png)

gif:

![alt text](https://github.com/EduardoGM98/MCOC2020-P3-G8/blob/main/Gif7.gif)

- Explique ¿como cambia el código para el caso 3-D? ¿Como se imponen las condiciones de borde?
  - En el codigo habria que agregar una variable "z" (dz) que sirva como variable de profundidad (para el modelo de elementos finitos) y forme de manera tridimensional los graficos. Con tres dimensiones se complejiza bastante el problema, ya que se necesitan mas condiciones de borde para poder solucionar y obtener las incognitas de temperatura dentro del hormigón. En 2D habian borde izquierdo, derecho, superior e inferior, pero en el caso 3D (pensandolo como un cubo) se necesitan saber mas condiciones de borde. De esta forma se lograria obtener los mismos resultados de esta entrega, pero en graficos tridimensionales que se apegan mas a la realidad. 
