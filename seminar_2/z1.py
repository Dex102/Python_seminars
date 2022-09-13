def check_digit(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

def sum_digits(number):
    sum = 0
    if float(number) < 0:
        number = abs(float(number))
    for digits in str(number):
        if digits != '.':
            sum += int(digits)
    return int(sum)

number = input('Input float number - ')

while True:
    if check_digit(number) == False:
        print('Error! Must be float number!')
        number = input('Input float number - ')
    else:
        print(f'The sum of the digits is {sum_digits(number)}')
        break