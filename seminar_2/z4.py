import datetime
from time import strftime

def check_digit(number):
    if number.isdigit():
        return True
    else:
        try:
            int(number)
            return True
        except ValueError:
            return False

def random_number(min, max):
    num = int(datetime.datetime.now().strftime('%f')) / 1000000
    num = int(num * (int(max) - int(min)) + int(min))
    return num

min_number = input('Input min number - ')
max_number = input('Input max number - ')

while True:
    if check_digit(min_number) == False or check_digit(max_number) == False:
        print('Error! Must be numbers!')
        min_number = input('Input min number - ')
        max_number = input('Input max number - ')
    else:
        print(f'Random digit is - {random_number(min_number, max_number)}')
        break