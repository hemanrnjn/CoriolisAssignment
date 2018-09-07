def translate(words_list):
    words = {
        "hello": 'hallå',
        "world": 'värld',
        "my": 'min',
        "name": 'namn',
        "is": 'är'
    }
    return list(map(lambda x: words[x] if x in words_list else x, words_list))


n = int(input('Enter the length of list\n'))
print('Enter the words of list\n')
words_list = []
while (n > 0):
    words_list.append(input())
    n -= 1
print('List of converted words is ', translate(words_list))
