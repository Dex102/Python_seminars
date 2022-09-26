number = input('Введите число для проверки - ')
list_of_strings = ['fsfs11', 'vxcvsdf22', 'eqrwsf33', 'fdser44', 'wertgrd55']
new_list = [i for i in list_of_strings if str(number) in i]
print(new_list)
result = lambda new_list:'Такой элемент есть в списке' if new_list else 'Такого элемента нет'
print(result(new_list))