# Write a Function that takes a type or object or variable as argument and returns True or False
# depending on whether the argument is an iterable or not. (Hint: Use the dir method to get a list
# of supported operations)
# def is_iterable(in_type):
# # write your code here to return True or False
# print(is_iterable(list)) # should print True
# print(is_iterable(int)) # should print False

def is_iterable(in_type):
    l = dir(in_type)
    if '__iter__' in l:
        return True
    else:
        return False


list = [1, 2, 3, 4, 5]
n = 10

print(is_iterable(list)) # should print True
print(is_iterable(int)) # should print False
