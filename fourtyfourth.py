import random


def generate_brackets(n):
    str = '['*n + ']'*n
    str_rand = ''
    while len(str) > 0:
        x = random.randint(0, len(str)-1)
        str_rand += str[x]
        str = str[0:x] + str[x+1:len(str)]
    print(str_rand)
    return str_rand


def valid_checker(str):
    stack = []
    flag = 0
    for ch in str:
        if ch == '[':
            stack.append('[')
        else:
            if len(stack):
                stack.pop()
            else:
                flag = 1
                break
    if flag == 1:
        print('NOT OK')
    else:
        print('OK')


n = int(input('Enter the number of brackets\n'))
valid_checker(generate_brackets(n))
