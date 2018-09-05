def mapping(list):
    for i in list:
        print(i, ' -> ', len(i), '\n')

n = int(input('Enter the length of list\n'))
print('Enter the elements of list\n')
list = []
while ( n > 0 ):
    list.append(input())
    n -= 1
mapping(list)