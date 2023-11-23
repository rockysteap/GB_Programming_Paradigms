# Структурное программирование

# Основная логика программы
def main():
    numbers = [38, 27, 43, 3, 9, 82, 10]

    # Сортировка слиянием
    if len(numbers) > 1:
        mid = len(numbers) // 2
        left_half = numbers[:mid]
        right_half = numbers[mid:]

        # Рекурсивно сортируем каждую половину
        main(left_half)
        main(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                numbers[k] = left_half[i]
                i += 1
            else:
                numbers[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            numbers[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            numbers[k] = right_half[j]
            j += 1
            k += 1

    print("Отсортированный список (структурно):", numbers)


if __name__ == "__main__":
    main()
