# Update the above program to work with both 3 character month and complete name of month.

import calendar
from calendar import monthrange


def getMonth(s1):
    if s1.lower() == 'jan' or s1.lower() == 'january':
        return 1
    elif s1.lower() == 'feb' or s1.lower() == 'february':
        return 2
    elif s1.lower() == 'mar' or s1.lower() == 'march':
        return 3
    elif s1.lower() == 'apr' or s1.lower() == 'april':
        return 4
    elif s1.lower() == 'may' or s1.lower() == 'may':
        return 5
    elif s1.lower() == 'jun' or s1.lower() == 'june':
        return 6
    elif s1.lower() == 'jul' or s1.lower() == 'july':
        return 7
    elif s1.lower() == 'aug' or s1.lower() == 'august':
        return 8
    elif s1.lower() == 'sep' or s1.lower() == 'september':
        return 9
    elif s1.lower() == 'oct' or s1.lower() == 'october':
        return 10
    elif s1.lower() == 'nov' or s1.lower() == 'november':
        return 11
    elif s1.lower() == 'dec' or s1.lower() == 'december':
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


month = input('Enter month in MMM/fullname format :')
y = int(input('Enter year in YYYY format :'))
print(days_in_month(y, month))
