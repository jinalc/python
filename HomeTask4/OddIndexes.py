# Print Elements at Odd indexes from a list (Using for loop)

l = [10, 11, 20, 21, 30, 31, 40, 41]

for i in range(len(l)):
    if i % 2 == 1:
        print(l[i])

