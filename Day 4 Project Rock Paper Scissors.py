import random

#Assign images to variables
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Create a list of those variables
game_images = [rock, paper, scissors]

#Take user's input number and convert it to an integer
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

#Print picture in list based on input (0 is the 1st item in Game_images list, 1 is 2nd item, 2 is 3rd item)
print(game_images[user_choice])

#The computer_choice variable is a random integer between 0 - 2
computer_choice = random.randint(0, 2)
print("Computer chose:")

#Print picture in list based on input (0 is the 1st item in Game_images list, 1 is 2nd item, 2 is 3rd item)
print(game_images[computer_choice])

#Account for invalid inputs by the user
if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 

    #Your rock beats scissors
elif user_choice == 0 and computer_choice == 2:
  print("You win!")

    #Your scissors loses to rock
elif computer_choice == 0 and user_choice == 2:
  print("You lose")

    #Since  rock is 0, paper is 1, and scissors is 2, if you choose a lower number than the computer you will lose
elif computer_choice > user_choice:
  print("You lose")

    #Since  rock is 0, paper is 1, and scissors is 2, if you choose a higher number than the computer you will win
elif user_choice > computer_choice:
  print("You win!")

    #If you make the same choice as the computer, it will be a draw
elif computer_choice == user_choice:
  print("It's a draw")
