def check_digit(number):
    if number.isdigit():
        return True
    else:
        try:
            int(number)
            return True
        except ValueError:
            return False

def check_quarter(number):
    if int(number) == 1:
        print('X > 0, Y > 0')
    elif int(number) == 2:
        print('X < 0, Y > 0')
    elif int(number) == 3:
        print('X < 0, Y < 0')
    elif int(number) == 4:
        print('X > 0, Y < 0')

quarter_number = input('Input number of quarter - ')

while True:
    if check_digit(quarter_number) == False:
        print('Error! Number of quarter must be integer digit(1-4)!')
        quarter_number = input('Input number of quarter - ')
    elif int(quarter_number) > 4 or int(quarter_number) < 1:
        print('Error! Number of quarter must be in 1-4')
        quarter_number = input('Input number of quarter - ')
    else:
        check_quarter(quarter_number)
        break
