import random


def guessing_game(guess, rand_num):
    if rand_num > guess:
        return 'Your guess is too Low'
    elif rand_num < guess:
        return 'Your guess is too high'
    else:
        return 'correct'


rand_num = random.randint(1, 20)
name = input('Hello! What is your name?\n')
print('Well ', name, ', I am thinking of a number between 1 and 20.')
c = 1
while True:
    n = int(input('Take a guess\n'))
    res = guessing_game(n, rand_num)
    if res == 'correct':
        print('Good job, ', name, '! You guessed my number in ', c, ' guesses!')
        break
    else:
        print(guessing_game(n, rand_num))
    c += 1
