def make_3sg_form(verb):
    if verb.endswith('y'):
        return verb[0:len(verb)-1] + 'ies'
    elif verb.endswith('o'):
        return verb + 'es'
    elif verb.endswith('ch'):
        return verb + 'es'
    elif verb.endswith('s'):
        return verb + 'es'
    elif verb.endswith('sh'):
        return verb + 'es'
    elif verb.endswith('x'):
        return verb + 'es'
    elif verb.endswith('z'):
        return verb + 'es'
    else:
        return verb + 's'

verb = input('Enter a verb\n')
print(make_3sg_form(verb))