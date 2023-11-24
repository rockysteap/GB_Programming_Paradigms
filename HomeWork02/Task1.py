"""
# В качестве подхода выбрано процедурное программирование в декларативном стиле
# в связи с тем, что это предоставляет возможность переиспользования процедурного
# кода в других проектах.

Таблица умножения
Домашнее задание
● Условие
На вход подается число n.
● Задача
Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
Обоснуйте выбор парадигм.
● Пример вывода:
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
..
1 * 9 = 9
"""


def print_multiplication_table(n: int = 10, cols: int = 8) -> None:
    """
    Печать таблицы умножения переданного размера в консоль.
    :param n: Размер таблицы умножения.
    :param cols: Количество столбцов при выводе.
    :return: Вывод таблицы в консоль.
    """
    s, e = 1, n if n <= cols else cols  # Определим start/end позиции для генератора.
    while True:
        offset = len(str(e * e))  # Определим смещение для форматированного вывода.
        matrix = ((a * b for a in range(s, e + 1)) for b in range(1, n + 1))
        for row_i, row in enumerate(matrix, 1):
            for item_i, item in enumerate(row, s):
                print(f'{str(row_i).rjust(offset)} *{str(item_i).rjust(offset)} =', end='')
                print(str(item).rjust(offset+1), end='  ')
            print()
        if e == n:
            break
        s, e = s + cols, e + cols if e + cols <= n else n
        print()


if __name__ == '__main__':
    print_multiplication_table(10, 5)
