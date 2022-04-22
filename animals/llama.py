from .animal import Animal

class Llama(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        # Establish the properties of each animal
        # with a default value
        self.walking = True
        self.shift = shift
        
    def feed(self):
        print(f"To feed {self.name} it's best to sing 'Rockytop' sung to it so it would eat its {self.food}")

# miss_fuzz = Llama()
# miss_fuzz.name = "Miss Fuzz"
# miss_fuzz.species = "domestic llama"

# print(miss_fuzz.name)
