def is_anagram(s1, s2):
    if len(s1) == len(s2):
        s1 = s1.lower()
        s2 = s2.lower()
        for i in s1:
            if i not in s2:
                return False
        return True
    else:
        return False

s1 = "Madam Curie"
s2 = "Radium came"
print('"', s1, '" and "', s2, '" are anagrams = ', is_anagram(s1, s2))
