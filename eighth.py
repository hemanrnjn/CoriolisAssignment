def is_Palindrome(str):
    c = 0
    f = 0
    for i in str:
        if c < len(str)/2:
            if (i.lower() != str[0-(c+1)].lower()):
                f = 1
                break
        else:
            break
        c += 1
    if f == 1:
        return False
    else:
        return True


if __name__ == '__main__':
    str = input('Enter a string\n')
    if is_Palindrome(str):
        print('Palindrome')
    else:
        print('Not Palindrome')
