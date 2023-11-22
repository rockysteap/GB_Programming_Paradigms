# Задача 2.
# Написать точно такую же процедуру, но в декларативном стиле.

from _my_lib.service import Service


def get_sorted_int_list_in_descending_order(lst: list) -> list:
    """
    Сортировка целочисленного списка по невозрастанию.
    Используется подход с копированием первоначального списка:
    Проходим по копии для поиска минимального и максимального значений.
    Добавляем найденные значения в новый список, а из копии удаляем.
    Пока копия не пустая - повторяем.
    :param lst: Список из целых чисел.
    :return: Отсортированный список из целых чисел.
    """
    return sorted(lst, reverse=True)


unsorted_list = Service.get_random_int_list()
print(unsorted_list)
sorted_list = get_sorted_int_list_in_descending_order(unsorted_list)
print(sorted_list)
