#Metodo de Gauss
#Solucion a Sistemas de Ecuaciones
#de la forma A * X = B

import numpy as np

A = np.array([[4,2,5],
             [2,5,8],
             [5,4,3]])
B = np.array([[60.70],
             [92.90],
             [56.30]])

casicero = 1e-15

#Para evitar truncamiento en las operaciones
A = np.array(A, dtype=float)

#Matriz Aumentada
AB = np.concatenate((A,B), axis = 1)
AB0 = np.copy(AB)

#Pivoteo parcial por filas
tamano = np.shape(AB)
n = tamano[0]
m = tamano[1]

print('antes AB \n', AB)
#para cada fila AB
for i in range(0, n-1,1):
    #columna desde diagonal i en adelante
    columns = abs(AB[i:,i])
    dondemax = np.argmax(columns)
    print(columns, dondemax)
    #dondemax no esta en diagonal
    if (dondemax !=0):
        #intercambia filas
        temporal = np.copy(AB[i,:])
        AB[i,:] = AB[dondemax + i , :]
        AB[dondemax + i , : ] = temporal
AB1 = np.copy(AB)
print('despues AB \n', AB)

#eliminacion hacia delante
for i in range(0, n-1, 1):
    pivote = AB[i,i]
    adelante = i+1
    print('pivote: ', pivote, '\n','adelante',  adelante)
    for k in range(adelante, n,1):
        factor = AB[k,i] / pivote
        AB[k,:] = AB[k,:] - AB[i,:] * factor
        print('factor:' ,factor, '\n', 'AB:' , AB)
AB2 = np.copy(AB)

#eliminacion hacia atras
ultfila = n-1
ultcolumna = m-1

i=ultfila
for i in range(ultfila,0-1, -1):
    pivote = AB[i,i]
    k = i -1
    atras=i-1
    for k in range(atras,0-1,-1):
        factor =AB[k,i]/pivote
        AB[k,:] = AB[k,:] - AB[i,:] * factor
    AB[i,:] = AB[i,:] / pivote

X = np.copy(AB[:, ultcolumna])


# SALIDA
print('Matriz aumentada: \n')
print(AB0)
print('Pivoteo parcial por filas: \n')
print(AB1)
print('eliminación hacia adelante: \n')
print(AB2.round(4))
print('Eliminacion hacia atras: \n')
print(AB.round(4))
print('Solucion: \n')
print(X.round(4))
