def char_freq(string):
    charDict = {}
    for i in string:
        if i in charDict:
            charDict[i] += 1
        else:
            charDict[i] = 1
    return charDict

string = input('Enter a string\n')
print(char_freq(string))