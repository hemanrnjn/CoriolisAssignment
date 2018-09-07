def histogram(list):
    for i in list:
        print(('*' * i) + '\n')

n = int(input('Enter the length of list\n'))
print('Enter the elements of list\n')
list = []
while (n > 0):
    x = int(input())
    list.append(x)
    n -= 1
histogram(list)
