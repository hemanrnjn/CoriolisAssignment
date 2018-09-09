def lingo(string, word):
    found = False
    res_str = ''
    if string == word:
        for i in string:
            res_str += '[' + i + ']'
        found = True
    else:
        word_char = list(word)
        string_char = list(string)
        i = 0
        for x in string_char:
            if x in word_char:
                if string_char[i] == word_char[i]:
                    res_str += '[' + string[i] + ']'
                else:
                    res_str += '(' + string[i] + ')'
            else:
                res_str += x
            i += 1
    return found, res_str


while True:
    string = input('Enter the word\n')
    word = 'tiger'
    if lingo(string, word)[0] is True:
        print(lingo(string, word)[1], '\n')
        break
    else:
        print(lingo(string, word)[1], '\n')
