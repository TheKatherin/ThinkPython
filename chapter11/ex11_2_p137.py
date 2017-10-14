def invert_dict(d):
    invers_d = dict()
    for key in d:
        invers_d.setdefault(d[key], []).append(key)
    return invers_d

d = dict({'a': 1, 'b': 1, 'c':2, 'd':1})
print(invert_dict(d))
