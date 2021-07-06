# Write the implementation for the map function yourself by the name my_map()

def my_map(funct, sequence):
    ans = []
    for ele in sequence:
        res = funct(ele)
        ans.append(res)
    return ans


seq = [1, 2]
funct = lambda x: x * x

result = my_map(funct, seq)
print(result)