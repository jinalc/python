# Write a program in python that stores alphabets from a to z in a text file

import string

try:
    f = open("test.txt", 'w', encoding='utf-8')
    f.write(string.ascii_lowercase)
finally:
    f.close()
