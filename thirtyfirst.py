def map(seq):
    new_seq = []
    for i in seq:
        new_seq.append(func(i))
    return new_seq


def func(x):
    return x+x


