import re
def correct(string):
    string = re.sub('\.', '. ', string)
    string = re.sub(' +', ' ', string)
    return string
string = input('Enter a string\n')
print(correct(string))