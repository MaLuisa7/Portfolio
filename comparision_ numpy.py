from numpy import *

a1 = array([10,30,50,70,100])
a2 = array([20,40,60,80,100])
a3 = array([1,2,3,4,5])
print(a1 > a2)
print(a1 < a2)
print(any(a1>=a2))
print(all(a1>=a2))
print(logical_or(a1 > 10, a1<101))
print(logical_and(a1 > 10, a1<101))
print(where(a3%2!=0, a3,0))
print(where(a2>a3, a2,a3))