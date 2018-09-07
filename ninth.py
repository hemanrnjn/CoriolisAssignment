def is_Member(x, list):
    f = 0
    for i in list:
        if x == i:
            f = 1
            break
    if f == 1:
        return True
    else:
        return False


if __name__ == '__main__':
    n = int(input('Enter the length of list and its elements\n'))
    list = []
    while (n > 0):
        list.append(input())
        n -= 1
    x = input('Enter the element to find\n')
    print(is_Member(x, list))
