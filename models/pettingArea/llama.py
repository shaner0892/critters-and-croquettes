# import the python datetime module to help us create a timestamp
from datetime import date

class Llama:

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
        
    def __str__(self):
        return f"{self.name} is a {self.species}"

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow" )

print(miss_fuzz.feed())

# miss_fuzz = Llama()
# miss_fuzz.name = "Miss Fuzz"
# miss_fuzz.species = "domestic llama"

# print(miss_fuzz.name)
