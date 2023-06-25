# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

FIRST_MULT_TABLE_1_MIN = 2
FIRST_MULT_TABLE_1_MAX = 5
FIRST_MULT_TABLE_2_MIN = 6
FIRST_MULT_TABLE_2_MAX = 9
SECOND_MULT_MIN = 2
SECOND_MULT_MAX = 10


def show_mult_table(first_mult_min, first_mult_max):
    print()
    for i in range(SECOND_MULT_MIN, SECOND_MULT_MAX + 1):
        line = []
        for j in range(first_mult_min, first_mult_max + 1):
            if i * j < 10:
                expression = f'{str(j)} X {str(i)} =  {str(j * i)}'
            elif i == 10:
                expression = f'{str(j)} X {str(i)}= {str(j * i)}'
            else:
                expression = f'{str(j)} X {str(i)} = {str(j * i)}'
            line.append(expression)
        for _ in line:
            print(_, end="     ")
        print()


print(" " * 18, "ТАБЛИЦА УМНОЖЕНИЯ")
show_mult_table(FIRST_MULT_TABLE_1_MIN, FIRST_MULT_TABLE_1_MAX)
show_mult_table(FIRST_MULT_TABLE_2_MIN, FIRST_MULT_TABLE_2_MAX)
