import datetime
class Event():
    def __init__(self, startTime, endTime, venue):
        self.startTime = startTime
        self.endTime = endTime
        self.venue = venue
        self.venue_list = []

    def addVenue(self, venue):
        self.venue_list.append(venue)


class Venue(Event):
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.address_list = []

    def addAddress(self, address):
        self.address_list.append(address)

class Address(Venue):
    def __init__(self, street, city, state, country):
        self.street= street
        self.city = city
        self.state = state
        self.country = country

obj1 = Event(datetime.date(2021,1,1),datetime.date(2022,1,1), 'Maria is learning more python programming')
print('Start date is {}, End date is {} and Venue is {}'.format(obj1.startTime, obj1.endTime, obj1.venue))

obj2 = Venue('Maria','Monte Catharina')
print('Name is {}, Address is {} '.format(obj2.name, obj2.address))
obj2.addAddress(obj2.address)
print(obj2.address_list)

obj3 = Address('Monte Catharina', 'Chihuahua', 'Chihuahua', 'Mexico')
print('Street is {}, City is {}, State is {}, Country is {}'.format(obj3.street,obj3.city,obj3.state,obj3.country))

obj2.addAddress(obj3.street)
obj1.addVenue('Maria is learning more pythoning things')

obj2.address_list
obj1.venue_list