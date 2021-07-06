# Modify the above program to count the occurrence of each symbol i.e. count of alphabet ‘a’,
# count of spaces, count of commas and so forth.

import sys

with open(sys.argv[1], 'r') as f:
    contents = f.read()
    d = dict()
    for x in contents:
        if x not in d:
            dict2 = {x: 1}
            d.update(dict2)
        elif x in d:
            count = d.get(x)
            dict2 = {x: count + 1}
            d.update(dict2)
    print(d)

# Run this command
# python FileHandling\CLIEx2.py FileHandling\reading.txt