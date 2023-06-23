# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна
# подсказывать «больше» или «меньше» после каждой попытки.
from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPTS = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)
count = 1

while count <= ATTEMPTS:
    print("Попытка №", count)
    expected_num = int(input("Введите число: "))
    if num == expected_num:
        print("Поздравляем, вы угадали! загаданное число ", num)
        break
    elif num > expected_num:
        print("Загаданное число больше")
    else:
        print("Загаданное число меньше")
    if count == ATTEMPTS:
        print("Попытки закончились. К сожалению, вы не угадали число. Загаданное число ", num)
    count += 1
