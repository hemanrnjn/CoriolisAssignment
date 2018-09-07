import time
import os


def speak_ICAO(string, delay_words, delay_ICAO_words):
    d = {
        'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta',
        'e': 'echo', 'f': 'foxtrot', 'g': 'golf', 'h': 'hotel',
        'i': 'india', 'j': 'juliett', 'k': 'kilo', 'l': 'lima',
        'm': 'mike', 'n': 'november', 'o': 'oscar', 'p': 'papa',
        'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
        'u': 'uniform', 'v': 'victor', 'w': 'whiskey',
        'x': 'x-ray', 'y': 'yankee', 'z': 'zulu'
    }
    words = string.split(' ')
    for word in words:
        for i in word:
            print(i)
            os.system("espeak " + d[i.lower()])
            time.sleep(delay_ICAO_words)
        time.sleep(delay_words)


string = input('Enter a string to speak in ICAO\n')
delay_words = float(input('Enter delay between words in second\n'))
delay_ICAO_words = float(input('Enter delay between ICAO words in second\n'))
speak_ICAO(string, delay_words, delay_ICAO_words)
