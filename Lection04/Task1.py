#  Императивная реализация
DIVISION_NUM = 5
arr = [i for i in range(100)]
res = []
for el in arr:
    res.append(el % DIVISION_NUM)
print(res)

# Функциональная реализация
DIVISION_NUM = 5
arr = [i for i in range(100)]
print(list(map(lambda x: x % DIVISION_NUM, arr)))
