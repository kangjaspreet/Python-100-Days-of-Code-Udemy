# A game of rock paper scissors

import random

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

choices = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors "))
if user_choice not in [0, 1, 2]:
	print("You chose an invalid option. You lose :(")
	exit()
else:
	print(f"You choose {choices[user_choice]}")

computer_choice = random.randint(0, 2)
print(f"Computer chooses {choices[computer_choice]}")

if user_choice > computer_choice:
	if user_choice == 2 and computer_choice == 0:
		print("You lose :(")
	else:
		print("You win!")
elif user_choice == computer_choice:
	print("It's a draw!")
else:
	if user_choice == 0 and computer_choice == 2:
		print("You win!")
	else:
		print("You lose :(")


