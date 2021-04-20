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

game_image = [rock, paper, scissors]
game_input = ['Rock','Paper','Scissor']
user_input = int(input('Select your choice. Choose 0 for Rock, 1 for paper and 2 for Scissor \n'))
print('Your input: ' + str(game_input[user_input]))
print(game_image[user_input])
computer_input = random.randint(0,2)
print('Computer input: ' + str(game_input[computer_input]))
print(game_image[computer_input])

if user_input > 3 or user_input <0:
    print('Invalid Input')
elif user_input == computer_input:
    print('Game Draw!')
elif user_input == 0 and computer_input ==2:
    print('You Win!')
elif user_input == 2 and computer_input ==0:
    print('Computer Wins!')
elif user_input > computer_input:
    print('You Win!')
elif user_input < computer_input:
    print('Computer Wins!')