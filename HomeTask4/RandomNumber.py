# Create a list of 5 random numbers and then print the list, sum of all numbers and average. Use
# a for loop.

# generate a random list
import random

randomlist = []
for i in range(0, 5):
    n = random.randint(1, 30)
    randomlist.append(n)

print('List of random numbers: ')
print(randomlist)

# sum of all numbers
sum = 0
for a in randomlist:
    sum = sum + a

print("Sum of all numbers: ")
print(sum)

# average of all numbers
print('Average of all numbers: ')
print(sum / 5)
