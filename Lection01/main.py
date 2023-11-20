"""
Сумма элементов массива в двух
# Пример императивного подхода:
arr = list(range(1, 11))
summ = 0
for item in arr:
    summ += item
print(summ)  # 55


# Пример декларативного подхода:
arr = list(range(1, 11))
print(sum(arr))  # 55

# Если в Py не было бы функции sum. Пример с reduce:
from functools import reduce
arr = list(range(1, 11))
res = reduce(lambda x, y: x + y, arr)
print(res)  # 55
"""


# Пример императивного процедурного подхода
# Поиск корней квадратного уравнения

def calculate_x(a, b):
    return -b / (2 * a)


def calculate_x1x2(a, b, D):
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    return x1, x2


# Расчет дискриминанта
def calculate_D(a, b, c):
    return (b * b) - 4 * a * c


def solve_for_x(a, b, c):
    D = calculate_D(a, b, c)
    if D > 0:
        return calculate_x1x2(a, b, D)
    elif D == 0:
        return calculate_x(a, b)
    else:
        return 'Нет действительных корней'


if __name__ == '__main__':
    a, b, c = 6, -17, 12

    solution = solve_for_x(a, b, c)

    print(solution)
