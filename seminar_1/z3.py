def check_digit(x, y):
    if x.isdigit() and y.isdigit():
        return True
    else:
        try:
            float(x)
            float(y)
            return True
        except ValueError:
            return False

def check_coord(x, y):
    if float(x) > 0 and float(y) > 0:
        print('1st quarter')
    elif float(x) < 0 and float(y) > 0:
        print('2nd quarter')
    elif float(x) < 0 and float(y) < 0:
        print('3rd quarter')
    elif float(x) > 0 and float(y) < 0:
        print('4th quarter')

x = input('Input X coordinate - ')
y = input('Input Y coordinate - ')

while True:
    if check_digit(x, y) == False:
        print('Error! X and Y must be digit!')
        x = input('Input X coordinate - ')
        y = input('Input Y coordinate - ')
    elif int(float(x)) == 0 or int(float(y)) == 0:
        print('Error! X and Y must be > 0!')
        x = input('Input X coordinate - ')
        y = input('Input Y coordinate - ')
    else:
        check_coord(x, y)
        break