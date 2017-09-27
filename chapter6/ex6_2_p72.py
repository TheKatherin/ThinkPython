def ack(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ack(m-1, 1)
    if m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))

print(ack(3, 2))
x = 0
print(chr(x))


# def ackermann(m, n):
#     """Computes the Ackermann function A(m, n)
#
#     See http://en.wikipedia.org/wiki/Ackermann_function
#
#     n, m: non-negative integers
#     """
#     if m == 0:
#         return n+1
#     if n == 0:
#         return ackermann(m-1, 1)
#     return ackermann(m-1, ackermann(m, n-1))
