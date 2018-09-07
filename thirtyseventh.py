def enumerate_file(file_name):
    file = open(file_name, 'r')
    new_file = open('enumerated-' + file_name, 'w')
    for i, line in enumerate(file):
        new_file.write('{}. {}\n'.format(i+1, line.strip()))
    file.close()
    new_file.close()


file_name = input('Enter the file name\n')
enumerate_file(file_name)
