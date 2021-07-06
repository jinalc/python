# Use reduce function and an appropriate lambda to find the maximum number in a list.

# importing functools for reduce()
import functools

# initializing list
list1 = [1, 3, 5, 6, 2, ]

#lambda function
max = lambda x , y: x if x > y else y

print("Maximum number is : {}".format(functools.reduce(max,list1)))
