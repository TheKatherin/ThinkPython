f = open("words.txt", "r")
d = dict()

for word in f.read().split():
    d[word] = 1 + d.get(word, 0)

string = "ipsum"
print(d.get(string))
