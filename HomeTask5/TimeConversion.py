# WAP to input number of seconds and print in days, hours, minutes and seconds
# ex: input = 10000
# Output = 0 day 2 hour 46 minute 40 second


def time_convertion(time):
    day = time // (24 * 3600)
    time = time % (24 * 3600)
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time
    print("D:H:M:S -> %d:%d:%d:%d" % (day, hour, minutes, seconds))


s = float(input('Enter time in seconds: '))
print('Given time in days, hours, minutes, seconds: ')
time_convertion(s)
