def filter_long_words(words_list, n):
    return list(filter(lambda x: len(x) > n, words_list))


n = int(input('Enter the length of list\n'))
words_list = []
print('Enter the words\n')
while n > 0:
    words_list.append(input())
    n -= 1
x = int(input('Enter the length or word to filter'))
print('Words longer than ', x, ' are\n' + filter_long_words(words_list, x))
