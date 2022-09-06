import modulos as mo

print(mo.sum(10,5))
print(mo.diff(10,5))


from modulos import *

print(sum(10,5))
print(diff(10,5))


from math import *
print(sqrt((9)))
print(ceil(8.2))
print(floor(7.9))
print(fabs(-2.2))

print(dir())

import math
help(math)


from random import *
print(random())
for i in range(10):
    print(random())
for i in range(10):
    print(randint(1,50))
for i in range(10):
    print(uniform(1,50))
for i in range(10):
    print(randrange(1,12,2))

lst = ['java', 'python', 'devops', 'aws']
for i in range(10):
    print(choice(lst))

