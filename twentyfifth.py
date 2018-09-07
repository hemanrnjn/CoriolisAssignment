def make_ing_form(verb):
    vowel = ['a', 'e', 'i', 'o', 'u']
    if len(verb) == 3:
        if (verb[-2] in vowel and not(verb[-1] in vowel) and
            not(verb[-3] in vowel)):
            return verb + verb[-1] + 'ing'
        elif verb.endswith('ie'):
            return verb[0:len(verb)-2] + 'ying'
        elif verb.endswith('e'):
            return verb[0:len(verb)-1] + 'ing'
        else:
            return verb + 'ing'
    elif verb.endswith('ie'):
        return verb[0:len(verb)-2] + 'ying'
    elif verb.endswith('e'):
        return verb[0:len(verb)-1] + 'ing'
    else:
        return verb + 'ing'


verb = input('Enter a verb\n')
print(make_ing_form(verb))
