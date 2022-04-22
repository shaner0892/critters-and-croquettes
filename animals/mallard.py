from .animal import Animal
from movements import Walking, Swimming

class Mallard(Animal, Walking, Swimming):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        Walking.__init__(self)

    def honk(self):
        print("The duck quacks a lot.")
    
    # run is defined in the Walking parent class, but also here. This run method will 
    # take precedence and Walking's run method will not be called by Goose instances
    def run(self):
        print(f'{self} waddles')
        
    def __str__(self):
        return f'{self.name} the duck'