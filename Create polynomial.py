# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:*
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
import os

os.system('cls||clear')

user_number = int(input("Введите степень многочлена: "))


def create_lst_polynomial(number):
    polynomial_lst = [0]*(number+1)
    polynomial_lst = [random.randint(0, 100) for i in polynomial_lst]

    return polynomial_lst


def print_polynomial(lst):
    string_polynomial = "" if lst[0] == 0 else str(
        lst[0])+"*x^"+str(len(lst)-1)
    for i in range(1, len(lst)-2):
        string_polynomial = string_polynomial + \
            "" if lst[i] == 0 else string_polynomial + \
            " + "+str(lst[i])+"*x^"+str(len(lst)-i-1)
    string_polynomial_last = "" if lst[-2] == 0 else " + "+str(lst[-2])+"*x"
    lst_last = "" if lst[-1] == 0 else " + "+str(lst[-1])
    return string_polynomial+string_polynomial_last+lst_last


user_polynomial = create_lst_polynomial(user_number)
print(user_polynomial)

printed_polynomial = print_polynomial(user_polynomial)
print(printed_polynomial)

polinomial_file = open("polynomial_file.txt", "w")
polinomial_file.writelines(printed_polynomial)
polinomial_file.close
