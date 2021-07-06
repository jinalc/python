# Write a function map_multiple that takes a list of functions/lambdas as first argument and a
# sequence type as second argument.
# The function picks first lambda from list, applies it to first element, then applies the second
# function to the result of first one and ….
# Similarly it does for each element and generates a mapping of input to output
# def map_multiple(functs, sequence):
#  # write definition here
# Ex: let list of lambdas be from question 1 and the list on numbers be [1,2,4]
#  So first function gives [1, 4, 16]
#  Second gives [1, 0.25, 0.0625]
#  Third gives [-1, -0.25, -0.0625]. Which is the final result.

def map_multiple(function, sequence):
    ans = []
    for num in sequence:
        result = num
        for f in function:
            result = f(result)
            ans.append(result)
    return ans


functs = [lambda x: x * x, lambda x: 1 / x, lambda x: x * -1]
l = [1, 4, 16, 64]

a = map_multiple(functs,l)
print(a)
