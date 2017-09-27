def print_n(s, n):
    if n > 0:
        print(s)
        n = n-1
        print_n(s, n)

print_n("Hello", 5)
