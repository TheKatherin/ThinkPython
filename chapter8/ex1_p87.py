def traversalwhile(string):
    index = 1
    while index <= len(string):
        letter = string[-index]
        print("string[-" , index, "] = ", letter)
        index = index + 1

def traversalwhile_v2(string):
    index = len(string) - 1
    while index >= 0:
        letter = string[index]
        print("string[-" , index, "] = ", letter)
        index = index - 1

traversalwhile("banana")
print("*****************************************************")
traversalwhile_v2("banana")


