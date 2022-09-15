def fib1(number):
    if number == 0:
        return 0
    elif number in [1,2]:
        return 1
    else:
        return fib1(number - 1) + fib1(number - 2)

def fib2(number):
    if number == -1:
        return 1
    elif number == -2:
        return -1
    else:
        return fib2(number + 2) - fib2(number + 1)


list1 = []

for i in range(9):
    list1.append(fib1(i))

list2 = []

for i in range(-8, 0):
    list2.append(fib2(i))

print(list2 + list1)

