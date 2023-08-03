# 2. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

my_list = [2, 4, 2, "k", "l", "k", 5, 5, 5, 7, 5]

result = []
for i in my_list:
    if my_list.count(i) > 1:
        if i not in result:
            result.append(i)
print(result)
