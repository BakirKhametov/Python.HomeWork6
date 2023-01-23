# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# number = int(input('Введите число: '))
# result = 0

# while number != 0:
#     residual_digit = number % 10
#     result = result + residual_digit
#     number //= 10
# print(result)

from functools import reduce

number = int(input('Введите число: '))
number = str(number)
new_numbers = list(map(int, number.strip()))
sum_number = reduce(lambda x, y: x + y, new_numbers)
print(sum_number)
# Снова невнимательно прочитал условия задачи и сделал решение для целых чисел. Сил и времени перерещать уже не осталось
#  Прошу понять и простить. 
