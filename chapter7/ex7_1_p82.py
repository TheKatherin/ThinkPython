import math

def mathsqrt(a, x):
    while True:
        print(x)
        y = (x + a/x) / 2
        if y == x:
            break
        x = y

def mysqrt(a):
    return math.sqrt(a)

def test_square_root():
    print('a'.ljust(5) + 'mysqrt(a)'.ljust(15) + 'math.sqrt(a)'.ljust(15) + 'diff'.ljust(20))
    print('-'.ljust(5) + '--------'.ljust(15) + '-----------'.ljust(15) + '----'.ljust(20))
    a=0.0
    while(a < 10.0):
        print('%.1f'.ljust(5) % a + '%.11f'.ljust(6) % mysqrt(a) + '%.11f'.ljust(6) % math.sqrt(a) + '%f'.ljust(6) % (mysqrt(a) - math.sqrt(a)))
        a = a + 1
    print()

test_square_root()

