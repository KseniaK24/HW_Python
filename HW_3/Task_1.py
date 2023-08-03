# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# 1) Какие вещи взяли все три друга
# 2) Какие вещи уникальны, есть только у одного друга и имя этого друга
# 3) Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

friend_and_things = {"misha": ("палатка", "спальник", "кружка", "вода", "спички"),
                     "pasha": ("спальник", "кружка", "спички", "фонарик", "зонт"),
                     "kate": ("спальник", "кружка", "вода", "фонарик", "котелок")}

friend_list = list(friend_and_things.keys())

result_1 = set(friend_and_things[friend_list[0]])
for i in range(1, len(friend_list)):
    things = set(friend_and_things[friend_list[i]])
    result_1 = result_1.intersection(things)
print("1)", *result_1)

print("2)")
for i in range(len(friend_list)):
    friends = friend_list[i]
    result_2 = set(friend_and_things[friends])
    temp = friend_list.pop(i)
    for j in range(len(friend_list)):
        things = set(friend_and_things[friend_list[j]])
        result_2 = result_2.difference(things)
    friend_list.insert(i, temp)
    print("  ", friends, *result_2)

print("3)")
for _ in range(len(friend_list)):
    friend = friend_list[0]
    result_3 = set(friend_and_things[friend])
    temp = friend_list.pop(0)
    friend_new = friend_list[0]
    things = set(friend_and_things[friend_new])
    for j in range(1, len(friend_list)):
        things_new = set(friend_and_things[friend_list[j]])
        things = things.intersection(things_new)
    result_3 = things - result_3
    print("  ", friend, *result_3)
    friend_list.append(temp)
