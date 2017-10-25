def half_line(x, y):
    print(x, end = ' ')
    for i in range(4):
        print(y, end = ' ')

def do_n_time(N, f, *args):
    for i in range(N):
        f(*args)
    print(args[0])

def full_square(size):
    for i in range(size):
        do_n_time(size, half_line, '+', '-')
        for y in range(4):
            do_n_time(size, half_line, '|', ' ')
    do_n_time(size, half_line, '+', '-')


full_square(2)
