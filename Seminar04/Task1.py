# Функция, которую мы хотим передать как аргумент
def square(x):
    return x ** 2

# Функция, принимающая другую функцию в качестве аргумента
def apply_function(func, value):
    return func(value)

# Присваиваем функцию переменной
my_function = square

# Вызываем функцию через переменную
result = apply_function(my_function, 5)

print(result)  # Вывод: 25
