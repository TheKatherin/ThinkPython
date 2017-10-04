def ducklings():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'
    suffix_ = 'uack'

    for letter in prefixes:
        if(letter == 'Q' or letter == 'O'):
            print(letter + suffix_)
        else:
            print(letter + suffix)

ducklings();


