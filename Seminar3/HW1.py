# Задача 16: Требуется вычислить, сколько раз встречается некоторое 
# число X в массиве A[1..N]. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. В последующих
#   строках записаны N целых чисел Ai. Последняя строка содержит число X



import random
N = int(input('Введите размер массива N: '))
X = int(input('Введите число X: '))
N_array = []
for i in range(N):
    N_array.append(random.randint(0, N//2))
print(f'Число вхождений посчитали с помощью встроенной функции count {N_array.count(X)}')

 