# Check which of the following declarations will work
# commented ones will not work


# d = {1=2,2=3}
# print(d)

d = {1: 2, 2: 3}
print(d)

# d = {1,2 : 2,3}
# print(d)

d = {(1, 2), (2, 3)}
print(d)

# d = {'a':'A', 'b': 1, c:[1234]}
# print(d)

d = {'a': 'A', 'b': 1, 'c': [1234]}
print(d)

d = dict([(1, 2), (2, 3)])
print(d)

d = dict(((1, 2), (2, 3)))
print(d)

# d = dict((1,2), (2,3)])
# print(d)

# d = dict('x'=2, 'y'=3)
# print(d)

# d = dict(1=2,2=3)
# print(d)
