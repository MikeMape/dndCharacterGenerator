import random
import time

stats = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]

strength = 0
dexterity = 0
constitution = 0
intelligence = 0
wisdom = 0
charisma = 0

userChoice = "yes"


# I'm going to use this function to roll the stats for
def rollStat():
    # setting the variables to global allows them to be accessed inside the function.
    global strength
    global dexterity
    global constitution
    global intelligence
    global wisdom
    global charisma
    numberOfRolls = 0
    roll = 0
    # this creates a list where the rolls will be stored
    rolls = []
    while numberOfRolls <= 3:
        # use the sorted property to put a list in numeric order.
        rolls.append(random.randint(1, 6))
        numberOfRolls = numberOfRolls + 1
    print("Alright lets roll four d6, drop the lowest one, and add them all up.")
    # print(rolls)
    # print("Let's get those sorted so we can drop the lowest one.")
    # time.sleep(2)
    rolls = sorted(rolls)
    # print(rolls)
    rolls.pop(0)
    # print(rolls)
    # time.sleep(1.5)
    # print("Aaaand here's the total.")
    print(sum(rolls))
    choice = input("Select the ability that you want this roll to represent: ")
    if choice.lower() in stats:
        if choice.upper() == "STRENGTH":
            strength = int(sum(rolls))
            return strength
        elif choice.upper() == "DEXTERITY":
            dexterity = sum(rolls)
            return dexterity
        elif choice.upper() == "CONSTITUTION":
            constitution = sum(rolls)
            return constitution
        elif choice.upper() == "INTELLIGENCE":
            intelligence = sum(rolls)
            return intelligence
        elif choice.upper() == "WISDOM":
            wisdom = sum(rolls)
            return wisdom
        elif choice.upper() == "CHARISMA":
            charisma = sum(rolls)
            return charisma
    else:
        print("Check your spelling and try again.")
    numberOfRolls = 0
    roll = 0
    rolls = []


def showStats():
    print("strength " + str(strength) + " dexterity " + str(dexterity) + " constitution " + str(
        constitution) + " intelligence " + str(intelligence) + " wisdom " + str(
        wisdom) + " charisma " + str(charisma))


while userChoice.upper != "EXIT":
    userInput = input("what would you like to do?")
    if userInput.upper() == "ROLLSTAT":
        rollStat()
    else:
        showStats()
