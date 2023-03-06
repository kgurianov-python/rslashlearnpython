import itertools
import random

# Make the computer pick a random choice out of the options Rock,Paper,Scissors

OPTIONS = ['rock', 'paper', 'scissors']


print(*itertools.combinations(OPTIONS, 2), sep='\n')


def comp_choice():
    choice = random.choice(OPTIONS)
    return (choice)


# Get the user's input
def user_choice():
    user_pick = ''
    while user_pick.lower() not in OPTIONS:
        user_pick = input(f'Choose between {OPTIONS}: ')
    return user_pick


# check who is the winner
def winner(comp, user):
    # rock beats scissors
    # paper beats rock
    # scissors beats paper
    if comp.lower() == user.lower():
        print('Its a DRAW!')
    elif (comp.lower() == 'rock' and user.lower() == 'scissors' or
          comp.lower() == 'paper' and user.lower() == 'rock' or
          comp.lower() == 'scissors' and user.lower() == 'paper'):
        print(f'Computer Wins it chose {comp}')
    else:
        print(f'You win, you chose {user}')


def replay(msg):
    return input(msg).lower().startswith('y')


# code to play the game
game_on = replay(f'Would you like to play a game of {", ".join([item.capitalize() for item in OPTIONS])}? Y or N:')
while game_on:
    user_pick = user_choice()
    comp_pick = comp_choice()
    winner(comp_pick, user_pick)
    game_on = replay('Do you want to play again? Enter Yes or No: ')

