# import the python datetime module to help us create a timestamp
from datetime import date

class Burro:

    def __init__(self, name, species, shift, food, chip_num):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True
        self.food = food
        self.__chip_number = chip_num
    
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
        
    @property # The getter
    def chip_number(self):
        return self.__chip_number # now foo.serial_num will actually return the private value. There is no actual serial_num attribute. So sneaky of us.
    
    @chip_number.setter # The setter
    def chip_number(self, number):
        pass # here, we simply tell the function to do nothing, effectively preventing the setting of a value for .serial_num. Without the setter, though, an attempt to assign a value to foo.serial_num would throw an Attribute Error and break stuff.
    
finn = Burro("Finn", "burro", "morning", "hay", 123789)

# This should not change the state of the object
finn.chip_number = 555783

# But printing it should work
print(finn.chip_number)
#prints 123789