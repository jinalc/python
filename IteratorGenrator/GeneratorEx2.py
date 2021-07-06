# Write a generator that takes a list and a predicate function (or lambda) as arguments and gives
# values after applying the lambda to the elements of the list. (The elements present in the list
# itself should not change)

def square_it(list, f):
    for x in list:
        yield f(x)


f = lambda x: x ** 2
list = [1, 2, 3, 4, 5]

# print result
a = square_it(list, f)
for i in a:
    print(i)

# check list element has not changed
print(list)