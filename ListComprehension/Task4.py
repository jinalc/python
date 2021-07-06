# Input a string from user, create a list of only those words whose length is more than 5
# characters.

s = input('Enter a sentence of different lengths of words: ')

print([words for words in s.split() if len(words) > 5])
