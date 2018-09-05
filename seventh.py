def reverse(str):
    s = ''
    for i in str:
        s = i + s
    return s

str = input('Enter a string\n')
print(reverse(str))