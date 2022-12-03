# 1 Вычислить число π c заданной точностью d
# *Пример:*
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import random
import math
import os

os.system('cls||clear')

user_accurate = 0.001
pi_stanadart = 3.14


def leibniz_series(accurate, pi):
    leibniz_pi = 0
    i = 1
    while abs(pi - leibniz_pi) > accurate:
        leibniz_pi = leibniz_pi + (4/i) - 4/(i+2)
        i = i + 4
    print(leibniz_pi)


def nilakant_series(accurate, pi):
    nilakant_pi = 3
    i = 2
    while abs(pi - nilakant_pi) > accurate:
        nilakant_pi = nilakant_pi + (4/(i*(i+1)*(i+2))) - 4/((i+2)*(i+3)*(i+4))
        i = i + 4
    print(nilakant_pi)


def arcsin_pi(accurate, pi):
    x = random.uniform(-1, 1)
    arcsin_pi = 2*(math.asin(math.sqrt(1-x**2))+abs(math.asin(x)))
    print(arcsin_pi, abs(arcsin_pi-pi) < pi)



leibniz_series(user_accurate, pi_stanadart)

nilakant_series(user_accurate, pi_stanadart)

arcsin_pi(user_accurate, pi_stanadart)


