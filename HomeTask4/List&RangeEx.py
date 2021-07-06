# WAP to input 10 numbers repeatedly (using range based for loop) and store them in a list.
# 11. Update the above program to also print the sum of numbers.

l = []
total = 0
for i in range(0, 10):
    ele = int(input('Enter a number: '))
    l.append(ele)
    total = total + ele
print(l)
print('Sum of all element is: ')
print(total)
