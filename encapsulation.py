#student

class Student:
    def __init__(self):
        self.id = 123
        self.name = 'John'

s = Student()
print(s.id)
print(s.name)


class Student:
    def __init__(self):
        self.__id = 123
        self.__name = 'John'


s = Student()
print(s.id)
print(s.name)
print(s.__id)
print(s.__name)

class Student:
    def __init__(self):
        self.__id = 123
        self.__name = 'John'

    def display(self):
        print(self.__id)
        print(self.__name)

s = Student()
print(s.display())
print(s._Student__id)
print(s._Student__name)

class Student:
    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

s = Student()
s.setId(123)
s.setName('Maria')
print(s.getId())
print(s.getName())


class Patient:
    def __init__(self):
        self.__id = 123
        self.__name = 'John'
        self.__ssn = 456

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setSsn(self, ssn):
        self.__ssn = ssn

    def getSsn(self):
        return self.__ssn

    def display(self):
        print(self.__id)
        print(self.__name)
        print(self.__ssn)

pa = Patient()
print(pa.getId())
print(pa.setId(896))
print(pa.getName())
print(pa.setName('Maria Luisa'))
print(pa.getSsn())
print(pa.setSsn(753))
print(pa.display())
print(pa._Patient__name)