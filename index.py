from animals import Alligator, Chameleon, Copperhead, GilaMonster, Ratsnake, Cow, Donkey, Goat, Llama, Pig, Burro, Frog, Goldfish, Koi, Mallard, Turtle
from attractions import PettingZoo, Wetlands, SnakePit

varmint_village = PettingZoo("Varmint Village", "critters that like to dig and scurry")# slither_inn = SnakePit("Slither Inn", "more snakes than an Indiana Jones movie")
# critter_cove = Wetlands("Critter Cove", "full of feathered friends and fantastic fish")

# dori = Goldfish("Dori", "Goldfish", "flakes")



# critter_cove.add_animal(dori)

# for animal in critter_cove.animals:
#     print(f'You can find {animal.name} the {animal.species} in {critter_cove.attraction_name}')
    

        
# stinky = Burro("Stinky", "burro", "afternoon", "barley hay")
# sven = Goat("Sven", "dwarf goat", "afternoon", "hay")
# sophia = Donkey("Sophia", "sicilian donkey", "evening", "carrots")

# brian = Alligator("Brian", "American Alligator", "chicken")
# matt = GilaMonster("Matt", "Gila Monster", "crickets")
# steven = Ratsnake("Steven", "Ratsnake", "rats")

shelly = Turtle("Shelly", "Snapping Turtle", "fish", 2905374)

print(shelly.feed())

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow", 31251)

print(miss_fuzz.feed())



donald = Mallard("Donald", "Mallard Duck", "plants", 9890)
donald.run()
donald.swim()
# dori = Goldfish("Dori", "Goldfish", "flakes")
varmint_village.add_animal(donald)
for animal in varmint_village.animals:
    print(animal)

# print("Varmint Village is where you can find cute and fuzzy creatures to cuddle, like:")
# for animal in varmint_village.animals:
#     print(f'* {animal.name} the {animal.species}')
    
# print("Slither Inn is where you'll find stupendous snakes of all sizes, like:")
# for animal in slither_inn.animals:
#     print(f'* {animal.name} the {animal.species}')
    
# print("Critter Cove is where you'll find feathered friends and fantastic fish, like:")
# for animal in critter_cove.animals:
#     print(f'* {animal.name} the {animal.species}')