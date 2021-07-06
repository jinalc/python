# Read help for zip and write a program that has two lists
# l1 = [1,2,3,4]
# l2 = [10,20,30,40]
# And converts them to a dictionary d containing { 1:10,2:20 …….}


# help(zip)

l1 = [1, 2, 3, 4]
l2 = [10, 20, 30, 40]

l = list(zip(l1, l2))
print(l)


# convert it to dict

def convertToDict(tup):
    di = dict(tup)
    return di


print(convertToDict(l))
