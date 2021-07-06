# WAP to count the number of words in a file.

f = open('a.txt', 'r')
count = 0
s = f.read()
l = s.split()

for x in l:
    count += 1
print(count)
f.close()
