import random

numbers = [random.randint(0, 10) for i in range(10)]
result = [numbers[i] * numbers[-1-i] for i in range(len(numbers)//2 + len(numbers)%2)]

print(numbers)
print(result)