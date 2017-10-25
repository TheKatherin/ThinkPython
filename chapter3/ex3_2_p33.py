def do_twice(f, value):
    f(value)
    f(value)

def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)

def print_spam(spam):
    print(spam)

do_four(print_spam, '*-*-*-*')
