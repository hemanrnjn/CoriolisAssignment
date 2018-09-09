import re


def sentence_splitter(file_name):
    file = open(file_name, 'r')
    string = file.read()
    print(re.sub(r'\. ', '.\n', string))
    file.close()


file_name = input("Enter the file name\n")
sentence_splitter(file_name)
