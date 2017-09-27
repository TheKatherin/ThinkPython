#part 1
def check_fermat(a, b, c, n):
    if n>2 and a**n + b**n == c**n:
        print('Holy smokes, Fermat was wrong!')
    else:
        print("No, that doesn't work")
#part 2
def take_value():
    a = input("Print a: \n")
    b = input("Print b: \n")
    c = input("Print c: \n")
    n = input("Print n: \n")

    check_fermat(int(a), int(b), int(c), int(n))

take_value()

