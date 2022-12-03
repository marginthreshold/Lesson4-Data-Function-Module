# 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# *Пример*
# - при N=236     ->        [2, 2, 59]

import os

os.system('cls||clear')

user_number = int(input("Введите натуральное число: "))


def factors_of_natural(number):
    i = 2
    lst = []
    while number/i != 1:
        if number % i == 0:
            number /= i
            lst.append(i)
        else:
            i += 1
    lst.append(i)
    print(lst)

factors_of_natural(user_number)

