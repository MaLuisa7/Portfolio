'''x = 1
while(x<=20):
    print(x)
    x +=1'''

# odd numbers
x =  int(input('Enter min number'))
y =  int(input('Enter max number'))

i = x
if i %2 == 0:
    i =x+1
    while i <=y:
        print(i)
        i +=2