strings = ['asd','qwe', 'zxc','qwe', 'ertqwe'] 
search = input('Введите строку для поиска - ')

print(strings)

try:
    second_element = [x for x in range(len(strings))[strings.index(search)+1::] if strings[x] == search]
    if second_element:
        print (f'Второе вхождение элемента под индексом: {second_element[0]}')
    else:
        print('Данного элемента нет')
except ValueError:
    print('Такого элемента нет в списке')