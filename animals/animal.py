# import the python datetime module to help us create a timestamp
from datetime import date

class Animal:
    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.food = food
        self.__chip_number = chip_num
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    
    @property # The getter
    def chip_number(self):
        return self.__chip_number # now foo.serial_num will actually return the private value. There is no actual serial_num attribute. So sneaky of us.
    
    @chip_number.setter # The setter
    def chip_number(self, num):
        pass # here, we simply tell the function to do nothing, effectively preventing the setting of a value for .serial_num. Without the setter, though, an attempt to assign a value to foo.serial_num would throw an Attribute Error and break stuff.
    
    def __str__(self):
        return f"{self.name} is a {self.species}"