# Императивное: Сортировка слиянием

def merge_sort(arr):
    # Проверяем, если список длиннее 1 элемента
    if len(arr) > 1:
        # Находим середину списка
        mid = len(arr) // 2

        # Разделяем список на две половины
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Рекурсивно сортируем каждую из половин
        merge_sort(left_half)
        merge_sort(right_half)

        # Инициализируем индексы для обхода левой и правой половин
        i = j = k = 0

        # Объединяем отсортированные половины обратно в исходный список
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Добавляем оставшиеся элементы из левой половины (если есть)
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Добавляем оставшиеся элементы из правой половины (если есть)
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Начальный список чисел
numbers = [38, 27, 43, 3, 9, 82, 10]

# Вызываем сортировку слиянием для этого списка
merge_sort(numbers)

# Выводим отсортированный список
print("Отсортированный список (императивно):", numbers)


quick_sort = sorted(numbers)
print("Отсортированный список (императивно):", quick_sort)
