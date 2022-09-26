import random

numbers = [random.randint(0, 10) for i in range(10)]
odd_elements = [numbers[i] for i in range(len(numbers)) if i % 2 != 0]
print(numbers)
print('Сумму элементов на нечетных позициях - ', sum(odd_elements))