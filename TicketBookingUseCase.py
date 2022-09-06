from threading import *

class BookMyBus:
    def buy(self):
        print('Confirming a seat')
        print('Processing the payment')
        print('Printing the Tickets')

obj = BookMyBus()
t1 = Thread(target= obj.buy)
t2 = Thread(target= obj.buy)
t3 = Thread(target= obj.buy)

t1.start()
t2.start()
t3.start()

###Add more logic

from threading import *

class BookMyBus:

    def __init__(self, availableSeats):
        self.availableSeats = availableSeats

    def buy(self, seatsRequested):
        print('Total Seats Available', self.availableSeats)
        if (self.availableSeats >= seatsRequested):
            print('Confirming a seat')
            print('Processing the payment')
            print('Printing the Tickets')
            self.availableSeats -= seatsRequested
        else:
            print('Sorry. Not seats available')

obj = BookMyBus(10)
t1 = Thread(target= obj.buy,args = (3,))
t2 = Thread(target= obj.buy,args = (4,))
t3 = Thread(target= obj.buy,args = (4,))

t1.start()
t2.start()
t3.start()
obj.availableSeats