import random


def find_word(prev):
    found = '',
    f = False
    for word in words:
        if prev[-1] == word[0]:
            found = word
            f = True
            words.remove(word)
            break
    return f, found


file_name = input('Enter File Name\n')
file = open(file_name, 'r')
words = file.read().split()
start = random.choice(words)
print('Child1 :', start)
x = 0
while True:
    res = find_word(start)
    if res[0] is True:
        if x == 0:
            print('Child2 :', res[1])
            x = 1
        else:
            print('Child1 :', res[1])
            x = 0
        start = res[1]
    else:
        break
file.close()
