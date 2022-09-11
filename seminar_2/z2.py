def check_digit(number):
    if number.isdigit():
        return True
    else:
        try:
            int(number)
            return True
        except ValueError:
            return False

def factorial(number):
    list_numbers = []
    for i in range(int(number)):
        if i == 0:
            list_numbers = [1]
        else:
            list_numbers.append(list_numbers[i - 1] * (i + 1)) 
    return list_numbers

number = input('Input int number - ')

while True:
    if check_digit(number) == False:
        print('Error! Must be int number!')
        number = input('Input int number - ')
    else:
        print(factorial(number))
        break