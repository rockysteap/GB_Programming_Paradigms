# Структура данных для представления студента
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


# Создание списка студентов
students = [
    Student("Alice", 22, 95),
    Student("Bob", 21, 88),
    Student("Charlie", 23, 92),
    Student("David", 22, 78),
]

# Вывод списка студентов
for student in students:
    print(f"Имя: {student.name}, Возраст: {student.age}, Баллы: {student.score}")




