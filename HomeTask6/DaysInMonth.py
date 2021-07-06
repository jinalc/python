# 6. WAF: days_in_month() that take name of month in 3 character format(MMM), and year (YYYY)
# as arguments and returns the number of days in the month.
# Use the function is_leap_year() to check the special case of 29 days in leap year for month of
# FEB. [Use dictionary to store the mapping of month and days.]

import calendar
from calendar import monthrange


def getMonth(s1):
    if s1.lower() == 'jan':
        return 1
    elif s1.lower() == 'feb':
        return 2
    elif s1.lower() == 'mar':
        return 3
    elif s1.lower() == 'apr':
        return 4
    elif s1.lower() == 'may':
        return 5
    elif s1.lower() == 'jun':
        return 6
    elif s1.lower() == 'jul':
        return 7
    elif s1.lower() == 'aug':
        return 8
    elif s1.lower() == 'sep':
        return 9
    elif s1.lower() == 'oct':
        return 10
    elif s1.lower() == 'nov':
        return 11
    elif s1.lower() == 'dec':
        return 12
    else:
        return 0


def days_in_month(y, mon):
    m = int(getMonth(mon))
    if m > 0:
        t = calendar.monthrange(y, m)
        return {mon, t[1]}
    else:
        return None


month = input('Enter month in MMM format :')
y = int(input('Enter year in YYYY format :'))
print(days_in_month(y, month))
