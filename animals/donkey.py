from .animal import Animal

class Donkey(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        # Establish the properties of each animal
        # with a default value
        self.walking = True
        self.shift = shift

# roberto = Donkey("Roberto", "alpaca", "midday")
# print(f'{roberto.name} the {roberto.species} is available to pet during the {roberto.shift} shift.')
# # prints Roberto the alpaca is available to pet during the midday shift.