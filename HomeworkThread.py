from threading import *


def DisplayEvenNumbers():
    for i in range(0,101):
        if i%2 ==0:
            print(i)


def DisplayOddNumbers():
    for i in range(0,101):
        if i%2 !=0:
            print(i)


obj_even = DisplayEvenNumbers()

obj_odd = DisplayOddNumbers()


t1 = Thread(target=DisplayEvenNumbers)
t2 = Thread(target= DisplayOddNumbers)

t1.start()
t2.start()



def MainAllNumbers():
    t1 = Thread(target=DisplayEvenNumbers)
    t1.start()
    t2 = Thread(target= DisplayOddNumbers)
    t2.start()

    t1.join()
    t2.join()

MainAllNumbers()