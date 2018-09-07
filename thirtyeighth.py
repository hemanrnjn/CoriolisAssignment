def calc_avg_len(file_name):
    file = open(file_name, 'r')
    words = file.read().split()
    c = sum = 0
    for word in words:
        sum += len(word)
        c += 1
    file.close()
    print(c, sum)
    return (sum * 1.00)/c


file_name = input('Enter the file name\n')
print('Average length of words in file is ', calc_avg_len(file_name))
