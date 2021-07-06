# Write a program to read a file and copy the contents to a new file such that the case gets
# reversed. i.e. upper case becomes lower case and vice versa.

# open both files
with open('a.txt', 'r') as firstfile, open('b.txt', 'w') as secondfile:
    # read content from first file
    for line in firstfile:
        secondfile.write(line.swapcase())