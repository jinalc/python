# 9. Write a program to input a string and print if it is palindrome or not.

s = input('Enter a string whether it is palindrome or not: ')

my_str = s.casefold()

rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
