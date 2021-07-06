# Write a program to read itself and print on the screen (Use Command Line Arguments).

try:
    f = open("reading.txt", 'r', encoding='utf-8')
    print(f.read())
finally:
    f.close()


# Using CLI:
import sys

with open(sys.argv[1], 'r') as f:
    contents = f.read()
    print(contents)

# Run this command
# python FileHandling\ReadAndPrint.py FileHandling\reading.txt
