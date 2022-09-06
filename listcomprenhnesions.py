#normalmente seria asi

'''lst =[]
for x in range(1,11):
    lst.append(x**3)
print(lst)'''
#list comprenhension equivalent to the function above
lst = []
lst = [x**3 for x in range(1,11)]

#evennumbers
lst = [x for x in range(1,21,2)]
print(lst)

lst = [x for x in range(1,21) if x%2 ==0]
print(lst)

#product of numbers in a list
a = [1,2,3,4,5]
b = [6,7,8,9,10 ]
z = []
'''for i in range(len(a)):
    z.append(a[i] * b[i])
   '''
z = [a[i]*b[i] for i in range(len(a))]
print(z)


## common elements in a list

a = [2,4,6,8]
b = [1,2,3,4]
result = []
'''
for i in a:
    if i in b:
        result.append(i)'''

result = [i for i in a if i in b]
print(result)

