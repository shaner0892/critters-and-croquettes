# import the python datetime module to help us create a timestamp
from datetime import date

class Pig:

    def __init__(self, name, species, shift, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

# wilbur = Pig("Wilbur", "pot-bellied pig")

# print(wilbur.name)