# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
from fractions import Fraction


def highest_common_factor(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if x % i == 0 and y % i == 0:
            hcf = i
    return hcf


number1 = input("Введите первую дробь: ")
number2 = input("Введите вторую дробь: ")

num1 = number1.split("/")
num2 = number2.split("/")
result_sum = []
result_mult = []

result_sum.append(int(num1[0]) * int(num2[1]) + int(num2[0]) * int(num1[1]))
result_sum.append(int(num1[1]) * int(num2[1]))
hcf1 = highest_common_factor(result_sum[0], result_sum[1])
if hcf1 != 1:
    result_sum[0] /= hcf1
    result_sum[1] /= hcf1

result_mult.append(int(num1[0]) * int(num2[0]))
result_mult.append(int(num1[1]) * int(num2[1]))
hcf2 = highest_common_factor(result_mult[0], result_mult[1])
if hcf2 != 1:
    result_mult[0] /= hcf2
    result_mult[1] /= hcf2

print(f'сумма дробей = {int(result_sum[0])}/{int(result_sum[1])}')
print(f'произведение дробей = {int(result_mult[0])}/{int(result_mult[1])}')

print(Fraction(number1) + Fraction(number2))
print(Fraction(number1) * Fraction(number2))
