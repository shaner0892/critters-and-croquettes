from .animal import Animal

class Alligator(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        # Establish the properties of each animal
        # with a default value
        self.slithering = True
        