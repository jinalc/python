# WAP to input a string and store ASCII values of all characters in a tuple.

s1 = input('Enter a String: ')

t = []

for i in range(len(s1)):
    t.append(ord(s1[i]))

T = tuple(t)
print(T)
