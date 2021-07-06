# WAF get_si() that takes Principle, Rate and Time as arguments and returns the Simple
# Interest.
# P x R x T ÷ 100


def get_si():
    P = int(input('Enter principal amount: '))
    R = int(input('Enter rate of interest: '))
    T = int(input('Enter time period in in years: '))
    return P * R * T / 100


print(get_si())
