import seventh as rev


def semordnilap(file_name):
    file = open(file_name, 'r')
    words = file.read().split()
    for i in words:
        for j in words:
            if i != j:
                if rev.reverse(j) == i:
                    print(i, ' ', j, '\n')
    file.close()


file_name = input('Enter the file name\n')
semordnilap(file_name)
