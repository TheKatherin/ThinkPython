def has_duplicates(t):
    for x in t:
        print("There is any duplicates in list ? = ")
        if t.count(x) > 1:
            return True
        else:
            return False

t = [1, 'a', 0, [1, 'a', 0]]
print(has_duplicates(t))

t = [1, 2, 3, 1]
print(has_duplicates(t))



