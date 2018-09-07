def check_vowel(ch):
    char = ch.lower()
    list = ['a', 'e', 'i', 'o', 'u']
    if char in list:
        print('True')
    else:
        print('False')

ch = ''
while True:
    ch = input('Enter a single character\n')
    if (len(ch) == 1 and ch.isalpha()):
        break
    else:
        print('Please enter only one and/or valid character')
check_vowel(ch)
