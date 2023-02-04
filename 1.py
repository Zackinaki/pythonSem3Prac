# 1 Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь
# в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел
#  Ai. Последняя строка содержит число X

# Пример:
# 5
# 1 2 3 4 5
# 3
# -> 1

import os
os.system('cls')

n = int(input("Vvdedite kol-vo elementov v spiske: "))

list_1 = [i for i in range(1, n+1)]
print(list_1)

x = int(input("Vvdedite iskomoe chislo: "))

print("Chislo", x, "vstrechaetsa v spiske", list_1.count(x), "raz")
