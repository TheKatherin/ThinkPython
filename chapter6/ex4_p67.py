def factorial(n):
    if not isinstance(n, int):
        print("Factorial is only defined for integers.")
        return None
    elif n < 0:
        print("Factorial is not defined for negative integers.")
        return None
    elif n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

print(factorial(9.50))
print(factorial(-7))
print(factorial(3))
