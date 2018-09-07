import seventeenth as palindrome


def read_palindrome(file_name):
    file = open(file_name, 'r')
    lines = file.read().split('\n')
    for line in lines:
        if palindrome.phrase_palindrome(line):
            print(line)


file_name = input('Enter File Name\n')
read_palindrome(file_name)
