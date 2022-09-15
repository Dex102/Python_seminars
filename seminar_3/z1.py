import random

def check_digit(number:str) -> int:
    while True:
        try:
            list_size = int(input(number))
            return list_size
        except ValueError:
            print('Error! Must be int number!')

def create_list(size:int) -> list:
    list_numbers = [random.randint(-10, 10) for _ in range(size)]
    return list_numbers

def sum_even(numbers:list) -> int:
    sum = 0

    for i in range(len(numbers)):
        if i % 2 != 0:
            sum += numbers[i]
    return sum

list_size = check_digit('Input int digit - ')
list_numbers = create_list(list_size)

result = sum_even(list_numbers)

print(list_numbers)
print(f'Sum of even elements is - {result}')

