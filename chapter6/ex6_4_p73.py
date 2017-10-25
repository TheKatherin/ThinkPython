def is_power(a,b):
    if(a%b != 0):
        return False
    elif(a/b == 1):
        return True
    else:
        return is_power(a/b,b)


print(is_power(5, 2))
