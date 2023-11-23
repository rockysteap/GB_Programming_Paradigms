# Структурное программирование

# Основная логика программы
def main():
    num1 = 10
    num2 = 5

    # Вычисление суммы
    result = num1 + num2
    print("Сумма:", result)

    # Вычисление разности
    result = num1 - num2
    print("Разность:", result)

    # Вычисление произведения
    result = num1 * num2
    print("Произведение:", result)

    # Вычисление частного
    if num2 != 0:
        result = num1 / num2
        print("Частное:", result)
    else:
        print("Деление на ноль недопустимо")


if __name__ == "__main__":
    main()
