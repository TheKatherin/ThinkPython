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
    print('a \t mysqrt(a) \t math.sqrt(a) \t diff' )
    print('-    --------     -----------     ----' )
    a=0.0
    while(a < 10.0):
        print(a, "\t", mysqrt(a),"\t", math.sqrt(a),"\t", abs(mysqrt(a) - math.sqrt(a)))
        a = a + 1
    print()

test_square_root()

