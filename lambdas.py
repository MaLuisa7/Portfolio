############# Lambda - cube of a given
def cube(n):
    return n**3

print(cube(2))

f = lambda n:n**3
print(f(2))

############# Lambda - Even or Odd
l = lambda x:'yes' if x%2==0 else 'no'
print(l(10))
print(l(9))

############# Lambda - Sum of 2 numbers
def add(a,b):
    return a+b
print(add(6,4))

l = lambda a,b: a+b
print(l(10,9))

############# Using a filter

lst = [10,2,13,30,45,89,21]
result = list(filter(lambda x: x%2 ==0 ,lst))
print(result)

############# Using the map function
lst = [10,2,13,30,45,89,21]
result =list(map(lambda x:x*2, lst))
print(result)

############# Using reduce function
from functools import reduce
lst = [10,2,13,30,45,89,21]
result =reduce(lambda x,y : x+y, lst)
print(result)