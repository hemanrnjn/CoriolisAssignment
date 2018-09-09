import random


def anagram(color_list):
    word = random.choice(color_list)
    ltr_list = list(word)
    anagram_str = ''
    while len(ltr_list) > 0:
        x = random.choice(ltr_list)
        ltr_list.remove(x)
        anagram_str += x
    print('Color word anagram: ', anagram_str, '\n')
    while True:
        string = input('Guess the color\n')
        if string.lower() == word:
            print('Correct!')
            break


color_list = ['black', 'brown', 'orange', 'blue', 'red', 'green']
anagram(color_list)
