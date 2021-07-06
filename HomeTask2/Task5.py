functs = [lambda x: x ** 0.5, lambda x: 1 / x]
l = [1, 4, 16, 64]

ans = []

for num in l:
    res = num
    for funct in functs:
        res = funct(res)
    ans.append(res)
print(ans)
