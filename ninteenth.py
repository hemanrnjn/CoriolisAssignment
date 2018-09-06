def sing_a_song():
    c = 99
    for i in range(0,99):
        print(c, 'bottles of beer on the wall, ', c, ' bottles of beer.\n',
        'Take one down, pass it around,', c-1, ' bottles of beer on the wall.')
        c -= 1

sing_a_song()