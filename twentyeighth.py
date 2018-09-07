import functools as f


def find_longest_word(words_list):
    word = f.reduce(lambda x, y: x if len(x) > len(y) else y, words_list)
    return len(word)


n = int(input('Enter the length of list\n'))
words_list = []
print('Enter the words\n')
while n > 0:
    words_list.append(input())
    n -= 1
print('Longest word\'s length is', find_longest_word(words_list))
