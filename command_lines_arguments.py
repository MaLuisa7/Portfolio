#class command lines arguments
import sys
lst = sys.argv

for i in lst: print(i)

print(len(lst))
print(lst[0])

#clase
lst  = sys.argv
print('Product is : ', lst[1] * lst[2])

#homework
accBalance = 10000
n = input(" Enter option number: \nOption 1:  Check Balance \nOption 2:  With Draw \nOption 3:  Deposit Cash \nOption 4:  Deposit Check \nTo end enter any other key")
n=int(n)
if n==1:
    checkbalance = print(accBalance)
elif n==2:
    withdraw = float(input('How much cash do you want to draw? : '))
    accBalance = accBalance - withdraw
elif n==3:
    cash = float(input('How much do you want to deposit: '))
    accBalance =accBalance + cash
elif n == 4 :
    check = float(input('How much do you want to deposit: '))
    accBalance =accBalance + check
else:
    print('Process finished')