from attractions import PettingZoo, SnakePit, Wetlands
from models.glassTank import Alligator, Chameleon, Copperhead, GilaMonster, Ratsnake
from models.pettingArea import Cow, Donkey, Goat, Llama, Pig, Burro
from models.pond import Frog, Goldfish, Koi, Mallard, Turtle


varmint_village = PettingZoo("Varmint Village")
slither_inn = SnakePit("Slither Inn", "more snakes than an Indiana Jones movie")
critter_cove = Wetlands("Critter Cove", "full of feathered friends and fantastic fish")


dori = Goldfish("Dori", "Goldfish", "flakes")



critter_cove.add_animal(dori)

for animal in critter_cove.animals:
    print(f'You can find {animal.name} the {animal.species} in {critter_cove.attraction_name}')
    

        
# stinky = Burro("Stinky", "burro", "afternoon", "barley hay")
# sven = Goat("Sven", "dwarf goat", "afternoon", "hay")
# sophia = Donkey("Sophia", "sicilian donkey", "evening", "carrots")

# brian = Alligator("Brian", "American Alligator", "chicken")
# matt = GilaMonster("Matt", "Gila Monster", "crickets")
# steven = Ratsnake("Steven", "Ratsnake", "rats")

# shelly = Turtle("Shelly", "Snapping Turtle", "fish")
# donald = Mallard("Donald", "Mallard Duck", "plants")
# dori = Goldfish("Dori", "Goldfish", "flakes")


# print("Varmint Village is where you can find cute and fuzzy creatures to cuddle, like:")
# for animal in varmint_village.animals:
#     print(f'* {animal.name} the {animal.species}')
    
# print("Slither Inn is where you'll find stupendous snakes of all sizes, like:")
# for animal in slither_inn.animals:
#     print(f'* {animal.name} the {animal.species}')
    
# print("Critter Cove is where you'll find feathered friends and fantastic fish, like:")
# for animal in critter_cove.animals:
#     print(f'* {animal.name} the {animal.species}')