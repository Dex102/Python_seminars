import z1 as funcs

def convert_to_2(number:int) -> str:
    new_string = ''
    while number > 0:
        new_string = str(number % 2) + str(new_string)
        number = number // 2
    return new_string

number = funcs.check_digit('Input int digit - ')

result = convert_to_2(number)

print(f'New number - {result}')