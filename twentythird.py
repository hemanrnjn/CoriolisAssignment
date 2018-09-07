import re


def correct(string):
    string = re.sub(r'\.', '. ', string)
    string = re.sub(r' +', ' ', string)
    return string


string = input('Enter a string\n')
print(correct(string))
