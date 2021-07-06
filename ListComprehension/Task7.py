# Write a list comprehension to store the following in a list: [Use nested and simple list
# comprehension both]
# [‘w’, ‘wo’, ‘wor’, ‘word’, ‘words’]

s = 'words'
l = []
for i in range(len(s)):
    l.append(s[0:i + 1])
print(l)

print([s[0:i + 1] for i in range(len(s))])
