# Создание списка студентов (как список списков)
students = [
    ["Alice", 22, 95],
    ["Bob", 21, 88],
    ["Charlie", 23, 92],
    ["David", 22, 78],
]

# Вывод списка студентов
for student in students:
    name, age, score = student
    print(f"Имя: {name}, Возраст: {age}, Баллы: {score}")