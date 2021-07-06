# 5. WAF: mean() that returns the mean of list of numbers passed to the function as argument.

def mean(l):
    n = len(l)
    sum = 0
    for x in l:
        sum = sum + x
    print('Mean of num of list is {}'.format(sum / n))


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mean(l)
