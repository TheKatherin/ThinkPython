def nested_sum(t):
    total = 0
    for mas in t:
        total += sum(mas)
    return total

t = [[1,2],[3,4,5,6]]
print("total = " , nested_sum(t))
