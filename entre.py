
help(print)
dir(help)

class House:
    def __init__(self, color):
        self.color = color

obj1 = House('Yellow')
obj1.color

class Window(House):
    def __init__(self, color, number):
        super().__init__(color)
        self.number = number
obj2 = Window('red', 5)

obj2.color
obj2.number