# WAP to input a string and print the ASCII value of each character in the string.


s1 = input('Enter a String: ')

for i in range(len(s1)):
    print("The ASCII value of %c  = %d" % (s1[i], ord(s1[i])))
