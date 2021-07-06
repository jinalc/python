# 7. WAP to find the length of hypotenuse of a right angled triangle, input the height and
# base from user.
# c = √(a² + b²)

import math


def calculateHypo(a, b):
    temp = a * a + b * b
    return math.sqrt(temp)


a = int(input('Enter height: '))
b = int(input('Enter base: '))

print('Hypotenuse of a right angled triangle is:')
print(calculateHypo(a, b))
