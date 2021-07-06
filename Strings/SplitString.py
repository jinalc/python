# 11. WAP to input Complete name and split it into first and last name and print it.
# also print after reversing each.
# Ex: if complete name is 'ab cd'
# then print 'dc ba'

s = input('Enter your full name: ')
l = s.split()
firstname = l[0]
lastname = l[1]

if len(l) > 2:
    for i in range(2, len(l)):
        lastname += ' '+l[i]

print('split: ')
print(firstname)
print(lastname)
print()
print('reverse: ')
print(firstname[::-1])
print(lastname[::-1])
