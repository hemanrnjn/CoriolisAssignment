import random


def find_word(prev):
    found = '',
    f = 0
    for word in words:
        if prev[-1] == word[0]:
            found = word
            f = 1
            words.remove(word)
            break
    return f, found


file_name = input('Enter File Name\n')
file = open(file_name, 'r')
words = file.read().split()
start = random.choice(words)
print('Child1: ', start)
res = find_word(start)
print('Child2: ', res[1])
x = 0
while res[0] == 1:
    start = res[1]
    res = find_word(start)
    if x == 0:
        print('Child1 :', res[1])
        x = 1
    else:
        print('Child2 :', res[1])
        x = 0
