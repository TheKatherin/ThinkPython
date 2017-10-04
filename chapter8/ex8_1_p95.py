t = [2,4,2,5,6,7,8,8,56,8,678,6,78,678,6]


def add_all(t):
    total = 0
    for x in t:
        total += x
    return total



t = ["sfsdf", "d", "zxc"]
def capitalize_all(t):
    res = []
    for s in t:
        t.append(s.capitalize())
    return t

print(capitalize_all(t))

