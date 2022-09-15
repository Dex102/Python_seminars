import random
import z1 as funcs

def create_list(size:int) -> list:
    list_numbers = [round(random.random() * 10, 2) for _ in range(size)]
    return list_numbers

def difference_elements(numbers:list) -> int:
    new_list = [i % 1 for i in numbers]
    diff = int((max(new_list) - min(new_list)) * 100)

    return diff


list_size = funcs.check_digit('Input int digit - ')
list_numbers = create_list(list_size)

result = difference_elements(list_numbers)

print(list_numbers)
print(f'Difference - {result}')