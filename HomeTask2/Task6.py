# Use filter function to filter a list of numbers and strings such that the result contains only
# numbers. (Hint : Use isinstance method)

seq = (1, 2, 4, '5', 'tyu', 7, 'bg', 8.0)
findInt = lambda x: isinstance(x, int)
integers = filter(findInt, seq)
print(list(integers))
