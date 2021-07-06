# Update the program again to count and print number of anagrams in the file.

f = open('a.txt', 'r')
count = 0
s = f.read()
l = s.split()

for i in range(len(l) - 1):
    if sorted(l[i]) == sorted(l[i + 1]):
        count += 1
        print(l[i])

print('Total Anagrams: ')
print(count)
f.close()
