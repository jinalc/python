# WAP get_ci() that takes Principle, Rate and Time as arguments and returns the
# Compound Interest.
# P(1 + R/100) ^ T

def get_ci():
    P = int(input('Enter principal amount: '))
    R = int(input('Enter rate of interest: '))
    T = int(input('Enter time period in in years: '))
    return (P * (pow((1 + R / 100), T))) - P


print(get_ci())
