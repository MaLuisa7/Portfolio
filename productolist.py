lst =[1,2,3,4,5]
prod = 1
for i in lst:
    prod *=i
print('product is :',prod)

#multiplicationtable

x = int(input("Enter a number for generating a table"))
for i in range(1,11):
    print(x, 'X ',i,'=', i*x)

#breakdemo
lst = [3,6,9,5,12]
for i in lst:
    if (i==5):
        break
    print(i)

#continue demo

x = 0
while x <=20:
    x += 1
    if x%3 == 0:
        continue
    print(x)

#assert
x = int(input('Enter a number greater than 10'))
assert x>10, 'wrong number entered'
print('U entered', x )