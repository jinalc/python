# WAP to take a string as a command line argument and print whether it is palindrome or not.


s = input('Enter a string to check whether it is palindrome or not: ')

print('Palindrome' if s == s[::-1] else 'Not Palindrome')