def calc_len(seq):
    count = 0
    for i in seq:
        count += 1
    return count

x = int(input('Enter 1 for string and 2 for List\n'))
if x == 1:
    str = input('Enter the string\n')
    print('Length of string is ', calc_len(str))
else:
    list = []
    print('Enter Elements of the List, Enter # when finished')
    while True:
        ele = input()
        if ele == '#':
            break
        else:
            list.append(ele)
    print('Length of List is ', calc_len(list))