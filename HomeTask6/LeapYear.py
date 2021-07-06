# WAF: is_leap_year() that takes a year as input and retuns True if year is leap year, otherwise
# false.


def is_leap_year(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                flag = True
            else:
                flag = False
        else:
            flag = True
    else:
        flag = False
    return flag


y = int(input('Enter any year to check whether it is leap year or not:'))
print(is_leap_year(y))
