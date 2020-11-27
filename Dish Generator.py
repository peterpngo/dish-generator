import random
import dgitemlist
import os
os.system('cls')

def mainMenu():
    input('Press Enter to initiate Dish Generator!')
    dishGenerator()

def goAgain():
    option = input('Enter "q" to quit or press "Enter" to Generate again!')
    if option == "q":
        q()
    elif option == "Q":
        q()
    else: 
        dishGenerator()

def q():
    quit

def dishGenerator():
    print("\nYour Dish: ")
    print("Protein: ", random.choice(dgitemlist.protein))
    print("Vegetable: ", random.choice(dgitemlist.vegetable))
    print("Starch: ", random.choice(dgitemlist.starch))
    print("Sauce: ", random.choice(dgitemlist.sauce))
    print("Garnish: ", random.choice(dgitemlist.garnish))
    print('\n\n')
    goAgain()


mainMenu()