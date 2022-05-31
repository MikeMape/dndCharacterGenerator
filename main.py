import random

differentRaces = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Halfling", "Half-Orc", "Human", "Tiefling"]
differentClasses = [""]
characterRace = None
numberOfCharacters = None


print("Welcome to my DnD random character generator.")


def races():
    characterRace = random.sample(differentRaces, 1)



print(characterRace)
