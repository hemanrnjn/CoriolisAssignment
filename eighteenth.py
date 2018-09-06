def pangram(string):
    str = string.lower()
    ascii = 97
    alphaList = []
    for i in range(0, 26):
        alphaList.append(ascii)
        ascii += 1
    for i in str:
        x = ord(i)
        if x in alphaList:
            alphaList.remove(x)
    if len(alphaList) > 0:
        print('Given string is not Pangram')
    else:
        print('Given string is Pangram')

string = input('Enter a string\n')
pangram(string)