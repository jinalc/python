# WAP to create a dictionary of numbers mapped to their negative value for numbers from 1-5.
# The dictionary should contain something like this:
# Do with both with and without range based for loop.
# {1:-1,2:-2,3:-3….}

r = [1, 2, 3, 4, 5]
d = dict()

for i in range(1, 6):
    d[i] = -i

print('With range function: ')
print(d)

for i in r:
    d[i] = -i

print('Without range function: ')
print(d)
