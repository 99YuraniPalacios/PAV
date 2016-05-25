import numpy
from travelplan import *

A=numpy.array([[0,3,6,2,3,3],[4,0,5,1,2,3],[3,5,0,4,2,7],[1,3,2,0,3,1],[1,4,2,9,0,4],[4,3,2,5,4,0]])
travelplan(A)
Chequeando la conformación de la matriz...
...OK

Calculando trayecto con menor costo
Desde 1 Hasta 4
Desde 4 Hasta 6
Desde 6 Hasta 3
Desde 3 Hasta 5
Desde 5 Hasta 2

Los viajes con menor tarifa son:
[2 1 2 2 4]

El costo total del viaje es:
11

A=numpy.array([[0,3,6,2,3,3],[4,0,5,1,2,3],[3,5,0,4,2,7],[1,3,2,0,3,1],[1,4,2,9,0,4],[4,3,2,5,4,1]])

travelplan(A)
Chequeando la conformación de la matriz...
ERROR: Uno de los elementos de la diagonal principal no es cero
No es posible completar el calculo

A=numpy.array([[0,3,6,2,3,3],[4,0,5,1,2,3],[3,5,0,4,2,7],[1,3,2,0,3,1],[1,4,2,9,0,4],[4,3,2,5,4,0]])
travelplan(A)
Chequeando la conformación de la matriz...
...OK

Calculando trayecto con menor costo
Desde 1 Hasta 4
Desde 4 Hasta 6
Desde 6 Hasta 3
Desde 3 Hasta 5
Desde 5 Hasta 2

Los viajes con menor tarifa son:
[2 1 2 2 4]
El costo total del viaje es:
11
A=numpy.array([[0,3,3,4,3,3],[4,0,5,1,2,3],[3,5,0,4,6,7],[1,3,2,0,3,1],[1,4,2,9,0,1],[4,3,6,5,4,0]])
 travelplan(A)
Chequeando la conformación de la matriz...
...OK

Calculando trayecto con menor costo
Desde 1 Hasta 2
Desde 2 Hasta 4
Desde 4 Hasta 6
Desde 6 Hasta 5
Desde 5 Hasta 3
Los viajes con menor tarifa son:
[3 1 1 4 2]
El costo total del viaje es:
11

A=numpy.array([[0,4,3,4,3,2],[4,0,5,7,2,3],[3,5,0,4,6,7],[1,3,2,0,3,5],[6,4,2,9,0,1],[4,3,6,5,4,0]])
travelplan(A)
Chequeando la conformación de la matriz...
...OK

Calculando trayecto con menor costo
Desde 1 Hasta 6
Desde 6 Hasta 2
Desde 2 Hasta 5
Desde 5 Hasta 3
Desde 3 Hasta 4
Los viajes con menor tarifa son:
[2 3 2 2 4]
El costo total del viaje es:
13

