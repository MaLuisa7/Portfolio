######### Decorator that doubles the result of a function

def decor(fun):
    def inner():
        result = fun()
        return result *2
    return inner

def num():
    return 5

resultfun = decor(num)
print(resultfun())

########## Using a decorator

def decor(fun):
    def inner():
        result = fun()
        return result *2
    return inner

@decor
def num():
    return 5

print(num())

########## Decorating Strings
def decorfunc(fun):
    def inner(n):
        result = fun(n)
        result = result + ' How are you?'
        return result
    return inner
@decorfunc
def hello(name):
    return 'Hello ' + name

print(hello('Maria '))

########## Decorator Chaining
def square(fun):
    def inner():
        n = fun()
        return n*n
    return inner

def half(fun):
    def inner():
        n = fun()
        return n/2
    return inner

@half
@square
def num():
    return 10

print(num())
