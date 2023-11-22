# Задача 1.
# Дан список целых чисел numbers.
# Необходимо написать в императивном стиле процедуру для сортировки чисел
# в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

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
    res = []
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        res.append(lst[0])
        return res

    tmp = lst[:]
    min_index = max_index = max_add_count = 0

    while True:
        min_changed = max_changed = False
        min_value = max_value = tmp[0]

        for i in range(len(tmp)):
            if min_value >= tmp[i]:
                min_value, min_index = tmp[i], i
                min_changed = True
            if max_value < tmp[i]:
                max_value, max_index = tmp[i], i
                max_changed = True

        if len(tmp) == 1:
            res.insert(max_add_count, min_value if min_changed else max_value)
            break

        if min_changed:
            res.insert(max_add_count, min_value)
            tmp.pop(min_index)

        if max_changed:
            res.insert(max_add_count, max_value)
            max_add_count += 1
            if min_changed:
                max_index = max_index if min_index > max_index else max_index - 1
            tmp.pop(max_index)

        if len(tmp) == 0:
            break

    return res


unsorted_list = Service.get_random_int_list()
print(unsorted_list)
sorted_list = get_sorted_int_list_in_descending_order(unsorted_list)
print(sorted_list)
