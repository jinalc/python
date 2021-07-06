# 12. WAP to input a string and split it into 2 halves. The string can be of any length
# Ex-1: Input = “String”
# S1 = Str
# S2 = ing
# Ex-2: Input = “words”
# S1 = wo
# S2 = ds

s = input('Enter any string to split it in two halves: ')
s1 = ''
s2 = ''
first_half = int(len(s) / 2)

for i in range(first_half):
    s1 += s[i]
print(s1)

for i in range(first_half, len(s)):
    s2 += s[i]
print(s2)
# simple way
print()
print(s[0:len(s) // 2])
print(s[len(s) // 2::])
