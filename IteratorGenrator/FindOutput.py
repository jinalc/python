l = [10, 20, 30, 40]
itr = iter(l)
print(next(itr), next(itr))
itr = iter(l)
print(next(itr), next(itr))

itr = [10, 20, 30, 40].__iter__()
print(itr.__next__(), itr.__next__())
itr = reversed([10, 20, 30, 40])
print(itr.__next__(), itr.__next__())


def num_gen(start, end, diff=1):
    while start < end:
        yield start
        start = start + diff


g1 = num_gen(10, 20)
g2 = num_gen(1, 10, 4)
print(next(g1))
print(next(g2))
g3 = iter(g1)
print(next(g3))
print(next(g2))
print(next(g1))

itr1 = range(10, 20)
itr2 = range(1, 10, 4)
print(next(itr1))
print(next(itr2))
itr3 = iter(itr1)
print(next(itr3))
print(next(itr2))
print(next(itr1))

# Which exception is raised upon reaching the last element of on iterable via its iterator.
# StopIteration exception

# Name the two methods that are required for the iterator protocol.
# An iterator should support the __next__ method.
