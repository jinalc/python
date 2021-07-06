# 3. WAF: maximum() to return the largest number in a list of numbers (do not use max
# function). Function takes a list or tuple of numbers as argument.

def maximum(l):
    max = l[0]
    for x in l:
        if x > max:
            max = x
    print('Maximum is: {}'.format(max))


l = [1, 12, 123, 4, 5, 67]
maximum(l)
