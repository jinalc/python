# WAP to input a number and print its factorial. Factorial is denoted by n!, where n is the number
#     whose factorial is to be found.
#         Ex: if n = 4 output should be 24
#         4! = 1x2x3x4 = 24

def factorial(x):
    n = 1
    while x > 0:
        n = n * x
        x -= 1
    return n


n = int(input('Enter a number:'))

print('Factorial of {} : '.format(n))
print(factorial(n))
