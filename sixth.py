def sum(list):
    s = 0
    for i in list:
        s += i
    return s


def multiply(list):
    m = 1
    for i in list:
        m *= i
    return m


x = int(input('Enter the size of list and elements\n'))
list = []
for i in range(0, x):
    n = int(input())
    list.append(n)
print('Sum of numbers in list ', sum(list))
print('Sum of numbers in list ', multiply(list))
