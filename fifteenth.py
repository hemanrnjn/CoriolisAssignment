def find_longest_word(list):
    max = 0
    word = ''
    for i in list:
        if len(i) > max:
            max = len(i)
            word = i
    return word

n = int(input('Enter the length of list\n'))
print('Enter the elements of list\n')
list = []
while ( n > 0 ):
    list.append(input())
    n -= 1
print('Longest word is ', find_longest_word(list))