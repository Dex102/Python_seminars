def check_digit(number:str) -> int:
    while True:
        try:
            list_size = input(number)
            return list_size
        except ValueError:
            print('Ошибка! Должно быть число')