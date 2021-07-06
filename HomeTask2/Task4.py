from functools import reduce

f = lambda x,y : x if x> y else y
l=[10, 30, 50, 30, 10]
num = reduce(f,l)
print(num)