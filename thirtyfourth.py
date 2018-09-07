import re


def char_freq(file_name):
    dict = {}
    file = open(file_name)
    string = re.sub('[^A-Za-z0-9]+', '', file.read())
    for i in string:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    for key in sorted(dict.keys()):
        print(key, ':', dict[key])
    file.close()


file_name = input('Enter the file name\n')
char_freq(file_name)
