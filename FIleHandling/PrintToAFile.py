

import sys

print('This message will be displayed on the screen.')

original_stdout = sys.stdout

with open('filename.txt', 'w') as f:
    sys.stdout = f
    print('This message will be written to a file.')
    sys.stdout = original_stdout
