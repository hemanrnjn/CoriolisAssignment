def translate(str):
    string = ''
    for i in str:
        ch = i.lower()
        list = ['a', 'e', 'i', 'o', 'u']
        if ch in list:
            string += i
        else:
            string += i + 'o' + i
    return string

str = input('Enter a string\n')
print(translate(str))
