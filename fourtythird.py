def anagram_builder(file_name):
    file = open(file_name, 'r')
    dict = {}
    word_list = file.read().split()
    for word in word_list:
        x = ''.join(sorted(list(word)))
        if x in dict:
            dict[x].append(word)
        else:
            dict[x] = [word]
    c = 1
    for i in dict.values():
        if len(i) > c:
            max_list = i
            c = len(i)
    file.close()
    return max_list


file_name = input('Enter the name of file\n')
print('Biggest Set Anagram is ', anagram_builder(file_name))
