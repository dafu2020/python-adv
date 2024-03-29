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

rps_list = [rock, paper, scissors]

print("Rock Paper Scissors Time!\n Show me whaddaya got!")
user_choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

while user_choice not in range(0, 2):
    print("Hello? Rock paper scissors here, check your input.")
    user_choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

user_icon = rps_list[user_choice]

pc_choice = random.randint(0, 2)
pc_icon = rps_list[pc_choice]

print("User:")
print(user_icon)
print("PC:")
print(pc_icon)

if user_choice == 0:
    if pc_choice == 0:
        print("Tied game, try  again.")
    elif pc_choice == 1:
        print("You LOSE")
    else:
        print("You WIN!!")
elif user_choice == 1:
    if pc_choice == 0:
        print("You WIN!!")
    elif pc_choice == 1:
        print("Tied game, try  again.")
    else:
        print("You LOSE")

elif user_choice == 2:
    if pc_choice == 0:
        print("You LOSE")
    elif pc_choice == 1:
        print("You WIN!!")
    else:
        print("Tied game, try  again.")
else:
    print("Hello? Rock paper scissors here, check your input.")

# game_images = [rock, paper, scissors]
#
# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# print(game_images[user_choice])
#
# computer_choice = random.randint(0, 2)
# print("Computer chose:")
# print(game_images[computer_choice])
#
# if user_choice >= 3 or user_choice < 0:
#   print("You typed an invalid number, you lose!")
# elif user_choice == 0 and computer_choice == 2:
#   print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#   print("You lose")
# elif computer_choice > user_choice:
#   print("You lose")
# elif user_choice > computer_choice:
#   print("You win!")
# elif computer_choice == user_choice:
#   print("It's a draw")
