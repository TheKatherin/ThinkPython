def is_triangle(a, b, c):
    if a>b+c or b>a+c or c>a+b:
        print("No")
    else: print("Yes")

def user_prompts():
    a = int(input("Write 1st stick's length: "))
    b = int(input("Write 1st stick's length: "))
    c = int(input("Write 1st stick's length: "))

    is_triangle(a, b, c)

user_prompts()
