l1 = eval(input('Enter a list of elements'))
print(l1)

l2 = []
for each_value in l1:
    if each_value not in l2:
        l2.append(each_value)

print(l2)


s1 = set(l1)
print(s1)

#vowel conters

word = input('Enter a word')
vowels = {'a', 'e', 'i', 'o', 'u'}
results ={}
for c in word:
    if c in vowels:
        results[c] = results.get(c,0) +1

for k,v in sorted(results.items()):
    print(k, 'is present', v,'times')

#More programs, handle employee details
n = int(input('Enter the number of employees'))
employees = {}
for i in range(n):
    name = input('Enter employee name')
    salary = input('Enter employee salary')
    employees[name] = salary
print('You can know the salary details by entering the name')
while True:
    name = input('Enter employee name')
    salary = employees.get(name,-1)
    if salary == -1:
        print('Employee does not exists')
    else:
        print('The salary of the employee is:', salary)
    choice = input('Do you want to know the salary of an other employee[yes|no]')
    if choice =='no':
        break

#ejercicio imprime los numeros menores a 100 y que si es multiplo de 10, no lo imprima
x = int(input('Enter a number'))
for x in range(x):
    if x %10 == 0 :
        continue
    if x >100:
        break
    print(x)

#imprimir numeros primos
n = int(input('Enter a number'))
primeFlag = True
for i in range(2,n-1):
    if n%i == 0:
        primeFlag = False

if primeFlag:
    print('Prime number')
else:
    print('Not a prime number')