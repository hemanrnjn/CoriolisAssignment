def make_ing_form(verb):
    if verb.endswith('e'):
        return verb[0:len(verb)-1] + 'ing'
    elif verb.endswith('ie'):
        return verb[0:len(verb)-2] + 'ying'
    elif len(verb) == 3:
        if (verb[-2] == 'a' or verb[-2] == 'e' or verb[-2] == 'i' or verb[-2] == 'o' or verb[-2] == 'u'):
            if
        else:
            return verb + 'ing'
    else:
        return verb + 'ing'

verb = input('Enter a verb\n')
print(make_ing_form(verb))