# WAP to input 2 string from command line and create a list of common words in both the
# strings.

s1 = input('Enter 1st String: ')
s2 = input('Enter 2nd String: ')
l = []

for words1 in s1.split():
    for words2 in s2.split():
        if words1 == words2:
            l.append(words1)
print(l)

print([words1 for words1 in s1.split() for words2 in s2.split() if words1 == words2])
