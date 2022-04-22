from .animal import Animal

class Burro(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True
    
finn = Burro("Finn", "burro", "morning", "hay", 123789)

# This should not change the state of the object
finn.chip_number = 555783

# But printing it should work
print(finn.chip_number)
#prints 123789