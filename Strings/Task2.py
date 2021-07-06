# val = input()  ### if we give input as Python language or language python
# if i want to see if python is present in val1 or not , how can i do that

# val = input('Enter a string: ')
# print('PYTHON' in val.upper())
#
# names = ['Subrat', 'Abhishek', 'Komal', 'India']
# print(names[-1][-1])

for x in range(5, 0, -1):
    print(x)

# write a function to merge the two lists into one sorted list
a = [3, 4, 6, 10, 11, 18]
b = [1, 5, 7, 12, 13, 19, 21]

c = a + b
c.sort()
print(c)

# Write a function to display the start position of given substring str2 in string str1 and return 1 if it is in the string else return -1
str1 = 'My name is Python'
str2 = 'nam'


def checkString(str2, str1):
    if str2 in str1:
        return str1.find(str2)
    else:
        return -1


print(checkString(str2, str1))
