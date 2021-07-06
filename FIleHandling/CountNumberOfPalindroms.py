# Update the above program to count the number of palindromes present in the file.

f = open('a.txt', 'r')
count = 0
s = f.read()
l = s.split()

for x in l:
    if x == x[::-1]:
        count += 1
        print(x)

print('Total Palindromes: ')
print(count)
f.close()
