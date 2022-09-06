from abc import abstractmethod

class TouchScreenLaptop:

    def __init__(self):
        pass

    @abstractmethod
    def scroll(self):
        print('you are scrolling')

    @abstractmethod
    def click(self):
        print('you are clicking')

class HP(TouchScreenLaptop):

    def scroll(self):
        print('you are scrolling in HP')

class DELL(TouchScreenLaptop):

    def scroll(self):
        print('you are scrolling in DELL')

class HPNotebook(HP):

    def click(self):
        print('you are clicking in HPnotebook')

class DELLNotebook(HP):

    def click(self):
        print('you are clicking in DELLnotebook')

laptop_dell = DELL()
laptop_dell.scroll()

laptop_hp= HP()
laptop_hp.scroll()

hpnotebook = HPNotebook()
hpnotebook.click()
hpnotebook.scroll()

dellnotebook = DELLNotebook()
dellnotebook.click()
dellnotebook.scroll()