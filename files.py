#open the file for writing
f = open('myfile.txt', 'w')
s = input('Enter text: ')
f.write(s)
f.close()

#open the file for writing multiple strings
f = open('myfile.txt', 'w')
print('Enter text (type # when you are done)')
s=''
while s!='#':
    s = input('Enter text: ')
    f.write(s + '\n')

f.close()

#open the file for reading
f = open('myfile.txt', 'r')
s = f.read()
print(s)
f.close()

#check is the file exists
import os, sys

if os.path.isfile('myfile.txt'):
    f = open('myfile.txt', 'r')
else:
    print('Files Does not exist')
    sys.exit()

s = f.read()
print(s)
f.close()