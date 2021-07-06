#  WAP to input a list of numbers and store in a tuple. Now input another number and print the
# index of this number in the tuple.

l = []
total = 0
n = int(input("Enter length of the list: "))
for i in range(0, n):
    ele = int(input('Enter a number: '))
    l.append(ele)

T = tuple(l)
print(T)

s = int(input('Enter a number from the tuple: '))

index = 0
for i in range(len(T)):
    if T[i] == s:
        index = i
print('Index is: ')
print(index)
