from .animal import Animal

class Turtle(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        # Establish the properties of each animal
        # with a default value
        self.swimming = True

    def feed(self):
        print(f"When feeding {self.name} it's best to sprinkle some carrots on top of the kale.")
        