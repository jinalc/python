# WAP to input a string and print individual characters in the string using for loop.

s1 = input('Enter a String: ')

for i in range(len(s1)):
    print("The Character at %d Index Position = %c" % (i, s1[i]))
