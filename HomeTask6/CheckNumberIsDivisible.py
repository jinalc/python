# WAP to input a number and check if number is divisible by both 5 and 7.

def checkNumber(n):
    if n%5 == 0 and n/7==0:
        print('Number is divisible by 5 and 7')
    else:
        print('Number is not divisible by 5 and 7')


n1 = int(input('Enter a number: '))
checkNumber(n1)