#Ejercicio if - else
x = int(input('Enter a number '))
if x%2 == 0:
    print(x, 'is even')
else:
    print(x, 'is odd')

#Ejercicios if, else, elif
y = int(input('Enter a number '))
if y ==0:
    print(y,'is zero')
elif y%2 == 0:
    print(y, 'is even')
else:
    print(y, 'is odd')

#Examen
math, physis, chemestry = [ int(x) for x in input('Enter the grade of math, physis and chemestry separated by space ').split() ]
if math>35 and physis>35 and chemestry >35:
    avg= (math + physis + chemestry) / 3
    print('The average is:  ',avg)
    if avg <=59:
        print('You have got a C')
    elif avg>=69:
        print('You have got a A')
    else:
        print('You have got a B')
else:
    print('you have fail the exams')