# Императивное: Сортировка пузырьком

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

numbers = [64, 25, 12, 22, 11]
bubble_sort(numbers)
print("Отсортированный список (императивно):", numbers)

# Декларативное:

quick_sort = sorted(numbers)
print("Отсортированный список (императивно):", quick_sort)


