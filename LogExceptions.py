import logging

logging.basicConfig(filename='mylog.log', level=logging.DEBUG)

try:
    f = open('myfile', 'w')
    a,b = [int (x) for x in input('Enter two numbers: ').split()] # 4 y 0
    logging.info('Division in progress')
    c = a/b
    f.write('writting %d into file' %c)
except ZeroDivisionError:
    print('Division by zero is not allowed')
    print('Plase enter a non zero number')
    logging.error('Division by zero')
else:
    print('you have entered a non zero number')
finally:
    f.close()
    print('File closed')
print('Code after the exception')
