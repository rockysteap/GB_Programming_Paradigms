# Изменяемое состояние (не функциональный стиль)
numbers = [1, 2, 3, 4]
total = 0
# print(id(total))

for num in numbers:
    total += num
    # print(id(total))


# Без изменяемого состояния (функциональный стиль)
numbers = [1, 2, 3, 4]
total = sum(numbers)  # Создается новое значение "total"
