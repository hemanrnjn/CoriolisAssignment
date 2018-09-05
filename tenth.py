# import ninth as isMember

n1 = int(input('Enter the length of first list and its elements\n'))
list1 = []
while (n1 > 0):
    list1.append(input())
    n1 -= 1

n2 = int(input('Enter the length of second list and its elements\n'))
list2 = []
while (n2 > 0):
    list2.append(input())
    n2 -= 1

f = 0

# for i in list1:
#     if isMember.is_Member(i, list2):
#         f = 1
#         break

for i in list1:
    for j in list2:
        if i == j:
            f = 1
            break

if f == 1:
    print('Intersects')
else:
    print('Doesn\'t Intersect')