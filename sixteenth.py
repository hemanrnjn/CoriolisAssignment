def filter_long_words(n, list):
    list2 = []
    for i in list:
        if len(i) > n:
            list2.append(i)
    return list2
n = int(input('Enter the length of list\n'))
print('Enter the elements of list\n')
list = []
while ( n > 0 ):
    list.append(input())
    n -= 1
n = int(input('Enter length of word to filter\n'))
print('List of words longer than ', n, ' characters are: \n', filter_long_words(n, list))