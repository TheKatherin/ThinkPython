def cumsum(t):
    res = []
    for i in range(len(t)):
        res.append(sum(t[:i+1]))
    return res

print(cumsum([1,2,3]))
