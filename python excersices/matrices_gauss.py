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

#sustitucion hacia atras
ultfila = n-1
ultcolumna = m-1
X = np.zeros(n,dtype=float)
print(X)

for i in range(ultfila, 0-1 , -1):
    suma = 0
    for j in range(i+1, ultcolumna,1):
        suma  = suma + AB[i,j] * X[j]
    b = AB[i, ultcolumna]
    X[i] = (b-suma) / AB[i,i]

X = np.transpose([X])

# SALIDA
print('Matriz aumentada:')
print(AB0)
print('Pivoteo parcial por filas')
print(AB1)
print('eliminación hacia adelante')
print(AB)
print('solución: ')
print(X)


#-----------------------------------------------------

import numpy as np
A = np.array([[2,1,-1],
              [-3,-1,2],
              [-2,1,2]])
b = np.array([8,-11-3])

print(A, 'antes')

N = len(b)
x = np.zeros(N)

for i in range(N-1):
    b[i] = b[i] / A[i][i]
    A[i] = A[i] / A[i][i]
    for k in range(i+1, N):
        b[k] = b[k] - A[k][i] * b[i]
        A[k] = A[k] - A[k][i] * A[i]

i=N-1
b[i] = b[i] / A[i][i]
A[i] = A[i] / A[i][i]
print(A,b)


