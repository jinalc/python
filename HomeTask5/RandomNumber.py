# WAP to generate 4 random numbers in the range 0-26 and print their average

import random

randomlist = []
for i in range(1, 4):
    n = random.randint(0, 26)
    randomlist.append(n)

print('List of random numbers: ')
print(randomlist)

# sum of all numbers
sum = 0
for a in randomlist:
    sum = sum + a

print("Sum of all numbers: ")
print(sum)
