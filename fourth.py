def check_vowel(ch):
    char = ch.lower()
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        print('True')
    else:
        print('False')

ch = ''
while True:
    ch = input('Enter a single character')
    if (len(ch) == 1 and ch.isalpha()):
        break
    else:
        print('Please enter only one and/or valid character')
check_vowel(ch)