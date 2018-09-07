def map_words(words_list, mode):
    words = {
        "hello": 1,
        "world": 2,
        "my": 3,
        "name": 4,
        "is": 5,
        "Himanshu": 6
    }
    transalted = []
    if mode == 1:
        for i in words_list:
            if i in words:
                transalted.append(words[i])
            else:
                transalted.append(0)
        return transalted
    elif mode == 2:
        return list(map(lambda i: words[i] if i in words else 0, words_list))
    else:
        return [words[i] if i in words else 0 for i in words_list]


n = int(input('Enter the length of list\n'))
words_list = []
print('Enter the words\n')
while n > 0:
    words_list.append(input())
    n -= 1
mode = int(input('Enter mode of mappping\n' +
'1. For-Loop\n 2. map() function\n 3. Using list comprehensions\n'))
print('Mapped List is', map_words(words_list, mode))
