import z1 as funcs

def multiplic_elements(numbers:list) -> list:
    new_list = [numbers[i] * numbers[- (i + 1)] for i in range(len(numbers) // 2)]

    if len(numbers) % 2 != 0:
        new_list.append(numbers[len(numbers) // 2] ** 2)

    return new_list

list_size = funcs.check_digit('Input int digit - ')
list_numbers = funcs.create_list(list_size)

result = multiplic_elements(list_numbers)

print(list_numbers)
print(f'New list - {result}')