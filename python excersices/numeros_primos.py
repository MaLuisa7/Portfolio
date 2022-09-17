numero = 1
limite = 100
while numero <= limite:
    contador = 1
    x = 0
    while contador <= numero:
        if numero % contador == 0:
            x = x +1

        contador = contador +1

    if x == 2 :
        print(numero)

    numero = numero + 1


### Otro ejemplo
num = int(input('Ingrese un numero: '))

if num>1:
    cont = 0
    for i in range(2,num):
        resto = num % i
        if resto ==0:
            cont= cont +1
    if cont ==0:
        print('El numero {} que ingreso el usuario es un numero primo'.format(num))
    else:
        print('El numero {} que ingreso el usuario no es un numero primo'.format(num))

else:
    print('el {} no es numero primo' .format(num))

## otro ejemplo de numero primo
num = int(input('Ingrese un numero: '))
if num>1:
    cont = 0
    i = 2
    while i<num and cont ==0:
        resto = num%i
        if resto==0:
            cont = cont +1
        i = i +1
    if cont ==0:
        print('El numero {} que ingreso el usuario es un numero primo'.format(num))
    else:
        print('El numero {} que ingreso el usuario no es un numero primo'.format(num))
else:
    print('el {} no es numero primo' .format(num))



