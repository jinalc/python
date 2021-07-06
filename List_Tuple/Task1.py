# 1. Convert a Tuple t = (1,2,3,4,5) to a list

t = (1, 2, 3, 4, 5)
l = list(t)
print(l)

# 2. WAP to join a list and a tuple:
# Store the result in a list LS
L = [1, 3, 5, 7]
T = (8, 6, 4, 2)
LS = L + list(T)
print(LS)


# 3. What is difference between list and tuple.
# 1	Lists are mutable	=== Tuples are immutable
# 2	Implication of iterations is Time-consuming	=== The implication of iterations is comparatively Faster
# 3	The list is better for performing operations, such as insertion and deletion.	=== Tuple data type is appropriate for accessing the elements
# 4	Lists consume more memory	=== Tuple consume less memory as compared to the list
# 5	Lists have several built-in methods	=== Tuple does not have many built-in methods.
# 6	The unexpected changes and errors are more likely to occur	=== In tuple, it is hard to take place.

# 4. Print the list in reverse order

def rev1():
    lst = [1, 2, 3, 4, 5, 6]
    lst.reverse()
    print('Using list.reverse() method: ')
    print(lst)


def rev2():
    lst2 = [1, 2, 3, 4, 5, 6]
    print('Using reversed() function: ')
    print(list(reversed(lst2)))


def rev3():
    lst3 = [1, 2, 3, 4, 5, 6]
    r = lst3[::-1]
    print('Using slicing:')
    print(r)


rev1()
rev2()
rev3()

# 5. Print Elements at Odd indexes from a list (Do not use loop)
l5 = [10, 11, 20, 21, 30, 31, 40, 41]

print("odd indexing", l5[1::2])

# 6. How many ways you can copy a list.
# https://www.geeksforgeeks.org/python-cloning-copying-list/

# 7. Predict output
n_list = ["Happy", [2, 0, 1, 5]]
print(n_list[0][1])
print(n_list[1][3])

# 8. Predict output
odd = [2, 4, 6, 8]
odd[0] = 1
print(odd)
odd[1:4] = [3, 5, 7]
print(odd)

# 10. Use the range method and create a tuple containing the following values:
# 	(20, 15, 10, 5)

l = []
for i in range(5, 21, 5):
    l.append(i)

l.reverse()
t = tuple(l)
print(t)
