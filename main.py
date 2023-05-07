# rook paper scissors
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
print('Rock paper scissor bot')
print('Welcome, you\'re playing rock paper scissors with Mary!')
user_choice = input('What do you choose? type "Rock", "Paper" or "Scissors".\n')
computer_choice = random.randint(1, 3)
if user_choice == 'Rock':
    if computer_choice == 1:
        print(rock)
        print(f'Mary chose:\n {rock}')
        print("It's a draw :3 Wanna Go Again?")
    elif computer_choice == 2:
        print(rock)
        print(f'Mary chose:\n {paper}')
        print('You lost! Mary wins YAY!')
    else:
        print(rock)
        print(f'Mary chose:\n {scissors}')
        print('You won! you got lucky this time :)')
elif user_choice == 'Paper':
    if computer_choice == 1:
        print(paper)
        print(f'Mary chose:\n {rock}')
        print('You won! you got lucky this time :)')

    elif computer_choice == 2:
        print(paper)
        print(f'Mary chose:\n {paper}')
        print("It's a draw :3 Wanna Go Again?")
    else:
        print(paper)
        print(f'Mary chose:\n {scissors}')
        print('You lost! Mary wins YAY!')
else:
    if computer_choice == 1:
        print(scissors)
        print(f'Mary chose:\n {rock}')
        print('You won! you got lucky this time :)')

    elif computer_choice == 2:
        print(scissors)
        print(f'Mary chose:\n {paper}')
        print('You lost! Mary wins YAY!')
    else:
        print(scissors)
        print(f'Mary chose:\n {scissors}')
        print("It's a draw :3 Wanna Go Again?")



