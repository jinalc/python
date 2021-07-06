# Use range based for loop to store all upper case alphabets and their corresponding ASCII
# values in the dictionary d.
# The result should be d = {‘A’: 65, ‘B’:66,…..}

# a = ord('A')
# print(a)

d = dict()
for i in range(65, 91):
    ascii = chr(i)
    d[ascii] = i

print(d)
