class Product :
    def __init__(self):
        self.name = 'IPhone'
        self.description = 'Its awesome'
        self.price = 700

p1 = Product()

print(p1.name)
print(p1.description)
print(p1.price)

p2 = Product()

print(p2.name)
print(p2.description)
print(p2.price)

####COURSE CLASS

class Course:
    def __init__(self, name, ratings):
        self.name = name
        self.ratings = ratings

    def average(self):
        numberOfRatings = len(self.ratings)
        average = sum(self.ratings) / numberOfRatings
        print('Average Ratings For ', self.name, 'Is ', average)

c1 = Course('Python', [10,10,9.9,10])
print(c1.name)
print(c1.ratings)
c1.average()

c2= Course('Java', [100,90,80,70])
print(c2.name)
print(c2.ratings)
c2.average()


### Programer

class Programmer:
    def setName(self, n):
        self.name = n

    def getName(self):
        return self.name

    def setSalary(self, sal):
        self.salary = sal

    def getSalary(self):
        return self.salary

    def setTechnologies(self, techs):
        self.tecnologies = techs

    def getTechnologies(self):
        return self.tecnologies

p1 = Programmer()
p1.setName('Maria')
p1.setSalary(10000)
p1.setTechnologies(['Java', 'Hibernate', 'Spring', 'Python'])

print(p1.getName())
print(p1.getSalary())
print(p1.getTechnologies())

class Product :
    def __init__(self):
        self.name = 'IPhone'
        self.description = 'Its awesome'
        self.price = 700

    def display(self):
        print(self.name)
        print(self.description)
        print(self.price)

p3 = Product()
p3.display()

class Student:
    mayor = 'CSE'

    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name

s1 = Student(1,'John')
s2 = Student(2, 'Maria')

s1.mayor
s2.mayor
s1.rollno
s2.rollno
s1.name
s2.name
Student.mayor

#Count the number of objects
class ObjectCounter:

    numberOfObjects = 0

    def __init__(self):
        ObjectCounter.numberOfObjects += 1

    @staticmethod
    def displayCount():
        print(ObjectCounter.numberOfObjects)

o1 = ObjectCounter()
o2 = ObjectCounter()

ObjectCounter.displayCount()

## Create an inner Class

class Car:

    def __init__(self, make, year):
        self.make = make
        self.year = year

    class Engine:
        def __init__(self, number):
            self.number = number

        def start(self):
            print('Engine started')

c = Car('bmw', 2017)
e = c.Engine(5)
e.start()

##Garbage collection methods

import gc

print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())


#Use destructor
class Product :
    def __init__(self):
        self.name = 'IPhone'
        self.description = 'Its awesome'
        self.price = 700

    def __del__(self):
        print('Inside the desctructor')

    def display(self):
        print(self.name)
        print(self.description)
        print(self.price)

p1 = Product()
p1.display()
p2 = Product()
p2.display()

#si me quiero asegurar de que el objecto se elimino
p1 = None


# Patient Clinicals Usecase
class Patient:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.clinical = []

    def addClinicalData(self, clinical):
        self.clinical.append(clinical)

class Clinical:

    def __init__(self, componentName, componentValue):
        self.componentName = componentName
        self.componentValue = componentValue

p = Patient('John', 40)
c1 = Clinical('bp', '80/120')
p.addClinicalData(c1)

c2 = Clinical('heartRate', 80)
p.addClinicalData(c2)

print(p.name)
for eachClinical in p.clinical:
    print(eachClinical.componentName)
    print(eachClinical.componentValue)

