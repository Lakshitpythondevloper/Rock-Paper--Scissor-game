import random as rd

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

games_background = [rock , paper , scissors]
user_input = int(input("Choose your weapon: 0 for rock, 1 for paper, or 2 for scissors: "))
print("You chose:")
print(games_background[user_input])
computer_number = rd.randint(0, 2)
print("I was chose this:")
print(games_background[computer_number])

if user_input >= 3 or user_input < 0:
    print("Sorry")
elif user_input == 1 and computer_number == 0:
    print("You win!")
elif user_input == 0 and computer_number == 1:
    print("Sorry! You lose this game.")
elif user_input == 2 and computer_number == 1:
    print("You win!")
elif user_input == 1 and computer_number == 2:
    print("Sorry! You lose this game.")
elif user_input == computer_number:
    print("This draw match!")