def translate(list):
    words = {
        "hello": 'hallå',
        "world": 'värld',
        "my": 'min',
        "name": 'namn',
        "is": 'är'
    }
    transalted = []
    for i in list:
        x = i.lower()
        if x in words:
            transalted.append(words[x])
        else:
            transalted.append(i)
    return transalted


n = int(input('Enter the length of list\n'))
print('Enter the words of list\n')
list = []
while (n > 0):
    list.append(input())
    n -= 1
print('Translated List is ', translate(list))
