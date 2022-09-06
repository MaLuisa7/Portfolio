#try and except

try:
    a,b = [int (x) for x in input('Enter two numbers: ').split()] # 4 y 0
    c = a/b
    print(c)
except ZeroDivisionError:
    print('Division by zero is not allowed')
    print('Plase enter a non zero number')
print('Code after the exception')


##### try, except and finally

try:
    f = open('myfile', 'w')
    a,b = [int (x) for x in input('Enter two numbers: ').split()] # 4 y 0
    c = a/b
    f.write('writting %d into file' %c)
except ZeroDivisionError:
    print('Division by zero is not allowed')
    print('Plase enter a non zero number')
finally:
    f.close()
    print('File closed')
print('Code after the exception')

##### try, except , else and finally

try:
    f = open('myfile', 'w')
    a,b = [int (x) for x in input('Enter two numbers: ').split()] # 4 y 0
    c = a/b
    f.write('writting %d into file' %c)
except ZeroDivisionError:
    print('Division by zero is not allowed')
    print('Plase enter a non zero number')
else:
    print('you have entered a non zero number')
finally:
    f.close()
    print('File closed')
print('Code after the exception')
