# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

remainder_two_digit = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
system_coding = 16
num = int(input("Введите целое число: "))
dividend = num
result = []

while dividend > 0:
    remainder = dividend % system_coding
    if remainder >= 10:
        result.append(remainder_two_digit[remainder])
    else:
        result.append(str(remainder))
    dividend = dividend // system_coding

print(''.join(result[::-1]))
print(hex(num))
