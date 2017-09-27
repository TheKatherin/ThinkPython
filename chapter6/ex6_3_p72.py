def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1: -1]

word = input('Want to see if it is a palindrome?\n')


def is_palindrome(word):
    if len(word) <= 2 and first(word) == last(word):
        print('True')
    elif first(word) == last(word):
        is_palindrome(middle(word))
    else:
        print('False')

is_palindrome(word)
