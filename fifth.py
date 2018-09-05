def translate(str):
    string = ''
    for i in str:
        ch = i.lower()
        if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == ' '):
            string += i
        else:
            string += i + 'o' + i
    return string

str = input('Enter a string\n')
print(translate(str))