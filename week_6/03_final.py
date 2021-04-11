tab = 2
start_day = 1
last_day = 31

print('\tS\tM\tT\tW\tT\tF\tS')
for i in range(tab):
    print('\t', end='')
for day in range(start_day, last_day+1):
    if day % 7 != 5:
        print('\t%d' % day, end='')
    elif day % 7 == 5:
        print('\t%d\n' % day)