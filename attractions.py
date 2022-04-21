

from models.glassTank.copperhead import Copperhead
from models.glassTank.ratsnake import Ratsnake


class PettingZoo:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute and fuzzy critters to cuddle"
        self.animals = list()
        
    def add_animal(self, new_animal):
        self.animals.append(new_animal)
        
class SnakePit:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "More snakes than an Indiana Jones movie"
        self.animals = list()
        
    def add_animal(self, new_animal):
        self.animals.append(new_animal)

    @property
    def last_critter_added(self):
        return f'{self.animals[-1]}'

class Wetlands:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "Full of feathered friends and fantastic fish"
        self.animals = list()
        
    def add_animal(self, new_animal):
        self.animals.append(new_animal)
        

    
slither_inn = SnakePit("The Slither Inn")
sammy = Copperhead("Sammy", "copperhead", "Ice Cube")
shalene = Ratsnake("Shalene", "rat snake", "rats...duh")

slither_inn.add_animal(sammy)
slither_inn.add_animal(shalene)

print(slither_inn.last_critter_added)
# prints Shalene the rat snake