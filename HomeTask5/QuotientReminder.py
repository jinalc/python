# WAP get_q_r() taking 2 numbers as parameters and returns the quotient and
# remainder in the form of a tuple.

def get_q_r(n1, n2):
    l = []
    q = int(n1 / n2)
    r = int(n1 % n2)
    l.append(q)
    l.append(r)
    T = tuple(l)
    return T


n1 = int(input('Enter a number: '))
n2 = int(input('Enter a number: '))

print('Quotient and remainder is: ')
print(get_q_r(n1,n2))
