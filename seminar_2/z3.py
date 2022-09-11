def check_digit(number):
    if number.isdigit():
        return True
    else:
        try:
            int(number)
            return True
        except ValueError:
            return False

def reversed_string(number):
    return ''.join(reversed(number))

def check_palindrom(original_string, reversed_string):
    if original_string == reversed_string:
        print('Digits is palindrom!')
        return True
    else:
        print('Digits is not palindrom!')
        return False

number = input('Input int number - ')
string_number = str(number)
reversed_string_number = reversed_string(string_number)

while True:
    if check_digit(number) == False:
        print('Error! Must be int number!')
        number = input('Input int number - ')
    else:
        if check_palindrom(string_number, reversed_string_number) != True:
            string_number = str(int(string_number) + int(reversed_string_number))
            reversed_string_number = reversed_string(string_number)
    break