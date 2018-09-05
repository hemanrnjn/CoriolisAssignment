def phrase_palindrome(string):
    str = string.lower().replace(' ', '').replace(',', '')
    c = 0
    f = 0
    for i in str:
        if c < len(str)/2:
            if (i != str[0-(c+1)]):
                f = 1
                break
        else:
            break
        c += 1
    if f == 1:
        print('Not Palindrome')
    else:
        print('Palindrome')

string = input('Enter a string\n')
phrase_palindrome(string)