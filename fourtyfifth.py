import random


def child_word_game(file_name):
    file = open(file_name, 'r')
    words = file.read().split()
    start = random.choice(words)
    prev = start
    for word in words:
        if word[]


file_name = input('Enter File Name\n')
child_word_game(file_name)
