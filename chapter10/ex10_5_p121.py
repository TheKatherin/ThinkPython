def is_sorted(t):
    print("Initial list = ", t)
    t_sort = sorted(t)
    print("List after sort = ", t_sort)
    return t == t_sort

t = ['a', 'b', 'c', 'e']
print(is_sorted(t))

t = ['a', 'f', 'b', 'c', 'e']
print(is_sorted(t))

t = [1, 2, 3, 8, 4, 5]
print(is_sorted(t))
