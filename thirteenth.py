def max_in_list(list):
    max = 0
    for i in list:
        if i > max:
            max = i
    return max

n = int(input('Enter the length of list\n'))
print('Enter the elements of list\n')
list = []
while ( n > 0 ):
    x = int(input())
    list.append(x)
    n -= 1
print ('Max number in given list is ', max_in_list(list))