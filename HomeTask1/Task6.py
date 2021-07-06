# 6. WAP to input a string s and a number n. Print the string n times on the screen,
# each should appear in a separate line (do not use any kind of loops, use the multiplication operator)

S1 = input("Enter a string: ")
S2 = input("Enter a no you want to repeat the above string: ")
S3 = str(S1 + '\n') * int(S2)
print(S3)