# Consider a list of words:
# Words = [‘Python’, ‘Object’, ‘Oriented’, ‘Language’]
# Write a loop to store the first character of each word in a list from the above list.
# Update the program to use list comprehension instead.


words = ['Python', 'Object', 'Oriented', 'Language']
l = []

for eachName in words:
    eachName = eachName[0]
    l.append(eachName)

print(l)

print([eachName[0] for eachName in words])
