# Write a program that take a file name as command line argument, opens it and then counts
# number of space characters in that file.


import sys

with open(sys.argv[1], 'r') as f:
    contents = f.read()
    space = ' '
    count = 0
    for space in contents:
        count += 1
    print(count)

# Run this command
# python FileHandling\CLIEx1.py FileHandling\reading.txt
