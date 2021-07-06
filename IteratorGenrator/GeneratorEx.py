# Write a generator, that generates Fibonacci numbers. The function takes a number as argument
# and generates numbers less than or equal to that number.

def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x + y
        if x <= nums:
            yield x


a = fibonacci_numbers(8)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))