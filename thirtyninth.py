import random


def guessing_game(guess):
    num = random.randint(1,20)
    if num > guess:
        return 'Your guess is too Low'
    elif num < guess:
        return 'Your guess is too high'
    else:
        return 'correct'


name = input('Hello! What is your name?\n')
print('Well ', name, ''', I am thinking of a number between 1 and 20.
    Take a guess.''')
while (guessing_game(int(input() is not 'correct'):
    print(guessing_game)