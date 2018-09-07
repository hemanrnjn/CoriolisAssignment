def generate_n_chars(n, ch):
    str = ''
    while (n > 0):
        str += ch
        n -= 1
    return str

print('Enter a character')
while True:
    ch = input()
    if len(ch) == 1 and ch.isalpha():
        break
    else:
        print('Please enter single and/or valid character\n')

n = int(input('Enter times to repeat\n'))
print(generate_n_chars(n, ch))
