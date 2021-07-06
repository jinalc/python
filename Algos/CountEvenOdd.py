# 2. WAF: count_even_odd() that counts and returns how many numbers are even and how
# many are odd in a list of numbers passed as argument.


def count_even_odd(list):
    evencount = 0
    oddcount = 0
    for x in list:
        if x % 2 == 0:
            evencount += 1
        else:
            oddcount += 1
    print("Even: {}".format(evencount))
    print("Odd: {}".format(oddcount))


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count_even_odd(l)
