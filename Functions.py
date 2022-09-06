def average(a,b):
    print(a)
    print(b)
    print('The average of two numbers are: ',(a+b)/2)

average(10,20)
average(a = 10,b= 20)
average(b = 10,a= 20)

def average(a=10,b=30):
    print(a)
    print(b)
    print('The average of two numbers are: ',(a+b)/2)

average(a =30, b=35)



def average2(a,b):
    return (a+b)/2

result = average2(10,20) # si queremos utilizar este resultado en otras partes del programa
print(result)

#calc
def calc(a,b):
    x = a + b
    y = a - b
    z = a * b
    u = a / b
    return x,y,z,u

result = calc(10,5)
print(result)

for i in result: print(i)

#local and global variables
x = 123
def display():
    x = 678
    print(x)
    print(globals()['x'])
display()

#accessing global variable with the same name
x = 123
def display():
    x = 678
    print(x)
    print(globals()['x'])
#assing function to a variable
z = display
z()

#Function inside another
def display(name):
    def message():
        return 'Hello '
    result = message() + name
    return result
display('Maria Luisa')
#print(message())

#Function as parameter to an other
def display(fun):
    return 'Hello ' + fun

def name():
    return 'Maria'

print(display(name()))


#returning fuctions

def display():
    def message():
        return 'Hello '
    return  message

fun = display()
print(fun())

## pass any type
def fun(lst):
    for i in lst:
        print(i)
fun([1,2,3,4])

#BMI Case

def calculateBMI(height, weight):
    heightInMeters = height * 0.4536
    bmi = weight / (heightInMeters * heightInMeters)
    return bmi

print(calculateBMI(48,1.48))


#args and kwargs
def myfun(x, *args, **kwargs):
    print(x)
    for each_args in args:
        print(each_args)
    for key, value in kwargs.items():
        print(key,value)

myfun(10,20,30,40,50, name = 'maria', sal = 100000000)


#passing optionals params to others functions
def myfun(x, *pos_params, **key_param):
    print(x)
    key_param['id'] = 123;
    for each_args in pos_params:
        print(each_args)
    for key, value in key_param.items():
        print(key,value)
    modified_pos_param = pos_params + (60,)
    my_fun2(*modified_pos_param, **key_param)

def my_fun2(*args, **kwargs):
    print(args)
    print(kwargs)

myfun(10,20,30,40,50, name = 'maria', sal = 100000000)
