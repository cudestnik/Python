
import random
N = int(input('Введите размер массива N: '))
X = int(input('Введите число X: '))
N_array = []
for i in range(N):
    N_array.append(random.randint(0, N//2))
print(f'Число вхождений посчитали с помощью встроенной функции count {N_array.count(X)}')

 