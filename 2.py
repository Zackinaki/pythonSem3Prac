# 2 Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N
# целых чисел Ai. Последняя строка
# содержит число X

# Пример:
# 5
# 1 2 3 4 5
# 6
# -> 5

import os
os.system('cls')

n = int(input("Vvdedite kol-vo elementov v spiske: "))

list_1 = [i for i in range(1, n+1)]
print(list_1)

x = int(input("Vvdedite iskomoe chislo: "))

k = list_1[0]

for i in range(n):
    if (abs(list_1[i]-x) < abs(k-x) or abs(list_1[i]-x) == abs(k-x) and list_1[i] < k):
        k = list_1[i]

print("Chislo", k, "v spiske ravnoe ili blizkoe k chislu", x)
