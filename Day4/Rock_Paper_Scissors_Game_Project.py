Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_image=[Rock, Paper, Scissors]
import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice >= 0 and choice <= 2:
    print(game_image[choice])

computer_choice = random.randint(0,2)
print("Computer Choice :")
print(game_image[computer_choice])

if choice >= 3 or choice < 0:
    print("You typed an invalid number. You lose!")
elif choice == 0 and computer_choice == 2:
    print("Congratulation You Win!")
elif computer_choice == 0 and choice == 2:
    print("You lose!, Better luck for next time.")
elif computer_choice > choice:
    print("You lose!, Better luck for next time.")
elif choice > computer_choice:
    print("Congratulation You Win!")
elif choice == computer_choice:
    print("Game Draw!, Try again")

