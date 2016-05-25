# Autora: Yurani Melisa Palacios Palacios 
# Fecha: 20 de Mayo 2016 

# SECOND HOMEWORK 

# Un vendedor tiene que viajar por 6 ciudades. El vendedor sabe que el costo para viajar de la ciudad i a la ciudad j es wij.
# Nite que estos costos se pueden alamacenar en una matriz cuadrada de tamano de 6x6.

# Dada la matriz W, disene un plan de viaje para el vendedor que recorra las 6 ciudades, de tal forma que minimize el valor total del viaje. 
# travelplan (W)



import numpy as np

# Analiza que la matriz este bien conformada

def chequearMatriz(W):
    print("Analizando la conformacion de la matriz...")
    M=np.matrix(W,dtype=np.int)
    n=M.shape

    if (n[0] == n[1]):
        for i in range(n[1]):
            if not(M[i,i] == 0):
                print("ERROR: Uno de los elementos de la diagonal principal no es cero")
                return False

        print("...OK")
        return True
    else:
        print("ERROR: Dimension incorrecta")
        return False


# FUNCION PARA REVISAR UNA FILA, BUSCAR EL VALOR MINIMO y RETORNAR EL VALOR CON SU POSICION
# RETORNA [Valor, fila, columna]

def valorMinimo(arr,fila):

    M=np.matrix(arr,dtype=np.int)
    n=M.shape
    referencia=np.array([M[fila,0],0,0])

    for i in range(n[1]):
        a=M[fila,i]

        if ((a<referencia[0]) and not(a==0)) or (not(a==0) and (referencia[0]==0)):
            referencia[0]=a
            referencia[1]=fila
            referencia[2]=i

    return referencia


# FUNCION QUE LLENA DE CEROS UNA COLUMNA

def llenarDeCeros(arr,columna):
    M=np.matrix(arr,dtype=np.int)
    n=M.shape
    for i in range(n[1]):
        M[i,columna]=0

    return M


def travelplan(W):
    if chequearMatriz(W) == True:
        M=np.matrix(W,dtype=np.int)
        n=M.shape
        solucion=np.zeros(n[1]-1,dtype=np.int)
        x=np.zeros(3,dtype=np.int)
        j=0
        print("Calculando trayecto con menor costo")
        while (j<n[1]-1):
            i=x[1]
            x=valorMinimo(M,i)
            print("Desde",x[1]+1,"Hasta",x[2]+1)
            xinv=np.array([x[0],x[2],x[1]],dtype=np.int)
            M=llenarDeCeros(M,i)
            solucion[j]=x[0]
            j=j+1
            x=xinv

        print("Los viajes con menor tarifa son:")
        print(solucion)
        print("El costo total del viaje es:")
        print(solucion.sum())
    else:
        print("No es posible completar el calculo")



	




















