import functools


def max_in_list(num_list):
    return functools.reduce(lambda a, b: a if a > b else b, num_list)


n = int(input('Enter the length of list\n'))
num_list = []
print('Enter the numbers\n')
while n > 0:
    num_list.append(int(input()))
    n -= 1
print('Largest Number is', max_in_list(num_list))
