#Choose your own adventure game

#ASCII Art and introduction
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("You're walking thorough a forest and you come to a fork in the road:")

#Forest fork in the road decision
decision_1 = input("Do you go left, or right?\n").lower()
if decision_1 == "left":

#River swim decision
    decision_2 = input("The weather turns and it starts to rain. Not wanting to spend the night in the forest,\n you take the path to the left and keep walking. As the forest starts to clear,\n you come to a large river thats blocking your path forward. what was a light drizzle\n is now a torrential downpour.You have two options, swim across to escape the forest,\n or wait until the rain clears.\n Do you swim, or wait?\n").lower()
    if decision_2 == "wait":

#Three Doors Decision
        decision_3 = input("Fatigue and weather considered, you fortify yourself at the edge of the forest and try to wait out the storm. Just as you start to fall asleep, lightning strikes the mountain beside you.\n A rockslide reveals 3 doors that you can choose to take shelter in: a RED door, a GREEN door, and a BLUE door. \n Which door do you choose? Red, green, or blue?\n ").lower()
        if decision_3 == "red":
            print("As soon as you turn the handle you instantly feel it heat up. \n suddenly fire bursts through the door way and burns you alive\n GAME OVER - YOU'VE BEEN BURNED ALIVE.")
        elif decision_3 == "green":
            print("As you turn the handle your nose is filled with the scent of reshly cut grass. \n Vines reach through the crack made by the door, growing form thin to trunk sized. The vines constrict and choke your last breaths from you\n GAME OVER - YOU'VE BEEN STRANGLED TO DEATH.")
        elif decision_3 == "blue":
            print("You turn the handle and hear the sound of clanking metal. Oppening the door fully, you see a chest with an open padlock on it.\n Opening the chest you find the entire contents of Jeff Bezos's net worth in gold coin and rare gem form. You've found what you were lookng for.\n YOU WIN!!!")
        else:
            print("You decide not to be tempted by either of the 3 options and fall asleep where you lie. A mountain lion finds you while you sleep and catches you before you can react.\n GAME OVER - YOU WERE EATEN ALIVE.")
    else:
        print("You take a chance and dive in the water, but the rain swell's the river and pulls you under the current. \n GAME OVER - YOU DROWNED")
else:
    print("The weather turns and it starts to rain. Not wanting to spend the night in the forest,\n you take the path to the right and keep walking.\nUnbeknownst to you, a trapper set various pits around the forest that have been widened & covered by the rain\n Your next step sends you plummiting to a pit of spikes, and you take your last breath\n GAME OVER - YOU DIED")

