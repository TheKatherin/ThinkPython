def right_justify(s):
    print(' ' * (70 - len(s)) + s) # use repeatable string
    print('1234567890' * 7)
    print(s.rjust(70)) # use addin function

right_justify('montly')
