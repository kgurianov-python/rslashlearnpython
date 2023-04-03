import logging

log_format = '%(asctime)s [%(name)s]  [%(levelname)s] : %(message)s'
logging.basicConfig(level=logging.DEBUG, format=log_format)
logger = logging.getLogger('logger')

from random import *

opt = ['rock', 'paper', 'scissors']
user_inp = input('Choose rock, paper, scissors or exit: ')
user_input = user_inp.lower()
i = 0
count = -1

if user_input == 'exit':
    print('GAME OVER')

elif user_input not in opt and user_input != 'exit':
    print('INVALID INPUT')

else:
    while count != 1:  ## Need help with this part
        computer_choice = opt[2]

        if user_input == computer_choice:
            print(user_input, ' <--> ', computer_choice, ' = DRAW')
            count = 0
            i += 1

        elif user_input == 'rock' and computer_choice == 'paper':
            print(user_input, ' <--> ', computer_choice, ' =  YOU LOST')
            count = 0
            i += 1

        elif user_input == 'rock' and computer_choice == 'scissors':
            print(user_input, ' <--> ', computer_choice, ' = YOU WON')
            count = 1
            i += 1
            break

        elif user_input == 'paper' and computer_choice == 'rock':
            print(user_input, ' <--> ', computer_choice, ' = YOU WON')
            count = 1
            i += 1
            break

        elif user_input == 'paper' and computer_choice == 'scissors':
            print(user_input, ' <--> ', computer_choice, ' = YOU LOST')
            count = 0
            i += 1

        elif user_input == 'scissors' and computer_choice == 'rock':
            print(user_input, ' <--> ', computer_choice, ' = YOU LOST')
            count = 0
            i += 1

        elif user_input == 'scissors' and computer_choice == 'paper':
            print(user_input, ' <--> ', computer_choice, ' = YOU WON')
            count = 1
            i += 1
            break

print('You won in ', i, 'turns.')


def main():
    pass


if __name__ == '__main__':
    main()
