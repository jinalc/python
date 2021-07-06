# Write a function that takes a list of numbers from user as argument and returns the sum of only
# odd numbers (Use only for loop. No need to use if statement).

def filter_odds(x):
    if x % 2 == 1:
        return True
    else:
        return False


def sum():
    l = []
    total = 0
    n = int(input("Enter length of the list: "))
    for i in range(0, n):
        ele = int(input('Enter a number: '))
        l.append(ele)
    print(l)
    filtered_odds = filter(filter_odds, l)
    for ele in filtered_odds:
        total = total + ele
    return total


print()
print('Sum of odd numbers: {}'.format(sum()))
