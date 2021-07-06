# Create a mapping of number to word from 0-9. (0:’zero’……)
# • Ask user for a single digit number and print the corresponding word format.
# • Print all keys of above dictionary
# • Print all Values of a dictionary
# • Print all Key and Value pairs of above dictionary

d = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

print('All keys: ')
print(d.keys())

print('All values: ')
print(d.values())

print('All key-value pairs: ')
print(d)

n = int(input('Enter a number from 0-9: '))
print(d.get(n))
