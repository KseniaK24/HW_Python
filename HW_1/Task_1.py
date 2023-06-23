# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

first_mult_table1_min = 2
first_mult_table1_max = 5
first_mult_table2_min = 6
first_mult_table2_max = 9
second_mult_min = 2
second_mult_max = 10


def show_mult_table(first_mult_min, first_mult_max):
    print()
    for i in range(second_mult_min, second_mult_max + 1):
        line = []
        for j in range(first_mult_min, first_mult_max + 1):
            if i * j < 10:
                expression = str(j) + " X " + str(i) + ' =  ' + str(j * i)
            elif i == 10:
                expression = str(j) + " X " + str(i) + '= ' + str(j * i)
            else:
                expression = str(j) + " X " + str(i) + ' = ' + str(j * i)
            line.append(expression)
        for _ in line:
            print(_, end="     ")
        print()


print(" "*18, "ТАБЛИЦА УМНОЖЕНИЯ")
show_mult_table(first_mult_table1_min, first_mult_table1_max)
show_mult_table(first_mult_table2_min, first_mult_table2_max)
