def reverse(str):
    s = ''
    for i in str:
        s = i + s
    return s


if __name__ == '__main__':
    str = input('Enter a string\n')
    print(reverse(str))
