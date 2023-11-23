# Процедурное программирование

# Функция для вычисления факториала числа
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Вычисление факториала числа 5
result = factorial(5)
print("Факториал числа 5 (процедурное):", result)
