day = int(input('Input day number - '))

if day == 6 or day == 7:
    print('Yes')
elif day > 7 or day < 0:
    print('7 days in a week!')
else:
    print('No')