# 1. Guess output of each slice:
s = 'Python is Object Oriented'
print(s[-1])
print(s[::-1])
print(s[:-1])
print(s[1:1])
print(s[4:10])

# 2. What error do you see for following statements:
# //index out of range
# s = ''
# print(s[1])

# 3. Do you get any error for the following code, if not give the output:
S = 'Landry'
print(S[1])

# 4. Find output of the following:
print('Find output of the following::::::::::::::::::::::::::::::')
# a)
s = 'a b cd'
print(len(s))
print(s[::2])
print(len(s[::2]))

# b)
s = 'a#b#c#d#'
print(s.split())
print(s.split('#'))
l = s.split('#')
s = '$'.join(l)
print(s)

# c)
S = 'Landry'
S = S[::-2][::-2]
# yda
# ay
print(S)

# d)
#false
print(1 > 2)

# e)
print(4 % 2, 5 % 2, 2 % 5, sep=',')

# f)
s = 'abcba'
s.upper()
print(s)
print(s.upper())
print(s.count('A'), end=',')
print(s.count('A', 2, 4), end=',')
print(s.count('a', 0, len(s)), end=',')


# 6. What does this symbol denote:
# 	[] >>> empty list

# 7. WAP to print all methods(functions/operations) available in a string (Hint : dir())
print()
print('dir() : ')
print(dir())
print('dir(str) : ')
print(dir(str))

# 8. Using the above method, get all methods available for str (strings) and join it into a space
# separated string. (use join and dir methods)
l = dir(str)
print('Using space : ')
print(" ".join(l))

# 9. Write statement to check if rstrip method is available in the str class.
# (Hint : Use the find function or in)
print('check rstrip method is available in the str class : ')
if 'rstrip' in dir(str):
    print('Yes it is')
else:
    print('No it is not')