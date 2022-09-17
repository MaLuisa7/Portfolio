def factorial(n):
    if n ==1 :
        return 1
    else:
        return n * factorial(n-1)

factorial(6)

#funcion de fibonacci sin recursividad
def fiib(n):
    a = 0
    b = 1
    for k in range(n):
        c = a + b
        a = b
        b = c
    return b
fiib(5)

#funcion de fibonacci CON recursividad
# caso base fn = fn-1 + fn-2
def fib_r(n):
    if n<2:
        return n
    return fib_r(n-1) + fib_r(n-2)

for x in range(20):
    print(fib_r(x))