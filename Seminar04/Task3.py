# Простой калькулятор на лямбда-выражениях в Python

# Операции калькулятора
add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y

while True:
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Выход")

    choice = input("Введите номер операции: ")

    if choice == '5':
        print("Выход из калькулятора.")
        break

    if choice not in ('1', '2', '3', '4'):
        print("Недопустимая операция. Пожалуйста, выберите операцию из списка.")
        continue

    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    if choice == '1':
        print("Результат:", add(num1, num2))
    elif choice == '2':
        print("Результат:", subtract(num1, num2))
    elif choice == '3':
        print("Результат:", multiply(num1, num2))
    elif choice == '4':
        if num2 == 0:
            print("Деление на ноль невозможно.")
        else:
            print("Результат:", divide(num1, num2))
