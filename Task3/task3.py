# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# import random

# n = int(input('Введите минимальное число рандомного списка: '))
# m = int(input('Введите максимальное число рандомного списка: '))
# list = []
# for i in range (m):
#     list.append (random.randint(n, m))
# print(list)

# sum = 0
# for i in range(len(list)):
#      if i%2 != 0:
#         sum = list[i] + sum
# else:
#     print(f'Сумма элементов списка, стоящих на нечётной позиции: {sum}')

from functools import reduce
import random

n = int(input('Введите минимальное число рандомного списка: '))
m = int(input('Введите максимальное число рандомного списка: '))
list = [random.randint(n, m) for i in range(m)]
print(list)
odd_numbers = [y for x,y in enumerate(list) if x%2 != 0]
print(odd_numbers)
sum_number = reduce(lambda x, y: x + y, odd_numbers)
print(sum_number)

