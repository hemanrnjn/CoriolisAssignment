def alternade(file_name):
    file = open(file_name, 'r')
    words = file.read().split('\n')
    for word in words:
        res = get_word(word, 2)
        w1 = res[0]
        w2 = res[1]
        if w1 in words and w2 in words:
            print('"' + word + '": makes "' + w1 + '" and "' + w2 + '"')


def get_word(word, n):
    iter = n-1
    c = 2
    w1 = w2 = ''
    i = 0
    for ch in word:
        if i == iter:
            w1 += ch
            iter = (n-1) + (c-1) * 2
            c += 1
        else:
            w2 += ch
        i += 1
    return w2, w1


file_name = input('Enter file name\n')
alternade(file_name)
