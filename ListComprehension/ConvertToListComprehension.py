# 1==========================
L = [10, 20, 30, 40]
D = []

for i in L:
    D.append(i / 10)

print(L)
print(D)
print([var / 10 for var in L])

# 2=========================
L = []
for x in range(10):
    if x % 2 == 0:
        L.append(x)

print(L)
print([var for var in range(10) if var % 2 == 0])

# 3==========================
words = 'aLphaBEts'
count = 0
for char in words:
    if char in 'aeiouAEIOU':
        count += 1
print(count)
print(len([char for char in words if char in 'aeiouAEIOU']))

# 4=========================
word = 'aLphaBEts'
new_word = []
for char in word:
    if char.isupper():
        new_word.append(char.lower())
    else:
        new_word.append(char.upper())

print(new_word)
print([c.lower() if c.isupper() else c.upper() for c in word])
