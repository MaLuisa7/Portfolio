#Duck tiping demo

class Duck:
    def talk(self):
        print('Quak, quak')

class Human:
    def talk(self):
        print('Hello')

def callTalk(obj):
    obj.talk()

d = Duck()
callTalk(d)

h = Human()
callTalk(h)

######## example 2

class Flight:
    def __init__(self, engine):
        self.engine = engine

    def startEngine(self):
        self.engine.start()

class AirbusEngine:
    def start(self):
        print('Starting Airbus engine')

class BoingEngine:
    def start(self):
        print('Starting BoingEngine engine')

ae = AirbusEngine()
f = Flight(ae)
f.startEngine()

be = BoingEngine()
f1 = Flight(be)
f1.startEngine()


#### plusOperator Polymorphism example

x = 10
y = 20
print(x +y)
s1 = 'Hello'
s2 = ' How are you'
print(s2 + s2)
l1 = [1,2,3]
l2 = [ 4,5,6]
print(l1 + l2 )
