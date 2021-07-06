# Write a program to read a file and copy it into a new file.

from shutil import copyfile

copyfile("a.txt", "b.txt")

# open both files
with open('a.txt', 'r') as firstfile, open('b.txt', 'a') as secondfile:
    # read content from first file
    for line in firstfile:
        # append content to second file
        secondfile.write(line)
