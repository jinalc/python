# Assume a list containing heights ft and inches in the form of a list of string
# Example : l = [‘5ft10in’, ‘5ft’, ….]
# Write a function to convert the heights to meter. Use map function along with your function to
# convert everything to m.

import re

l = ['5ft10in', '5ft']


def meter_convert(height):
    l = re.findall(r'\d+', height)
    ft = int(l[0])
    if len(l) > 1:
        inches = int(l[1])
    else:
        inches = 0
    tot_inches = ft * 12 + inches
    meters = tot_inches * 0.0254
    return meters


meter = lambda x: meter_convert(x)

result = map(meter, l)
print(list(result))
