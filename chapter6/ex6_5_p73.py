def gcd(a, b):
    if b == 0:
        return a
    r = a % b
    return gcd(b, r)

print(gcd(27,12))


