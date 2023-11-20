def counting_sort(arr):
    # Находим максимальное и минимальное значения в массиве
    max_value = max(arr)
    min_value = min(arr)

    # Вычисляем диапазон значений
    range_of_values = max_value - min_value + 1

    # Создаем счетчик для хранения количества каждого элемента
    count = [0] * range_of_values

    # Заполняем счетчик
    for num in arr:
        count[num - min_value] += 1

    # Восстанавливаем отсортированный массив
    sorted_arr = []
    for i in range(range_of_values):
        sorted_arr.extend([i + min_value] * count[i])

    return sorted_arr

# Пример использования
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Отсортированный массив:", sorted_arr)



from collections import Counter

def counting_sort(arr):
    """
    Сортирует массив целых чисел с использованием сортировки подсчетом.

    Args:
        arr (list): Список целых чисел, которые нужно отсортировать.

    Returns:
        list: Отсортированный список целых чисел.

    Raises:
        ValueError: Если входной список пуст.
    """
    if not arr:
        raise ValueError("Входной список не может быть пустым.")

    max_value = max(arr)
    min_value = min(arr)
    counter = Counter(arr)
    sorted_arr = [num for num in range(min_value, max_value + 1) for _ in range(counter[num])]
    return sorted_arr

# Пример использования
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Отсортированный массив:", sorted_arr)
