# WAF: is_alphabet() that takes a string argument and returns True or False. True if all characters
# in the string are alphabets otherwise False. (write code using for loop and if. Do not use built in
# functions)

# built in function
# check_s1 = s1.isalpha()

# >>> help(string) # on Python 3
# ....
# DATA
#     ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
#     ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     digits = '0123456789'
#     hexdigits = '0123456789abcdefABCDEF'
#     octdigits = '01234567'
#     printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
#     punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
#     whitespace = ' \t\n\r\x0b\x0c'

import string


def check_s1(s1):
    for i in range(len(s1)):
        if s1[i] in string.ascii_letters:
            flag = True
        else:
            flag = False
            break
    return flag


s1 = input('Enter any string: ')
print(check_s1(s1))
