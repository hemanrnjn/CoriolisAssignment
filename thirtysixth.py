def find_hapax(file_name):
    dict = {}
    file = open(file_name, 'r')
    words = file.read().split()
    for word in words:
        if word.lower() not in dict:
            dict[word.lower()] = 1
        else:
            dict[word.lower()] += 1
    for word in words:
        if dict[word.lower()] == 1:
            print(word, '\n')
    file.close()


file_name = input('Enter the file name\n')
find_hapax(file_name)
