# Поведенческий паттерн 'Стратегия'
# Интерфейс для стратегии сортировки
class SortingStrategy:
    def sort(self, data):
        pass


# Конкретная стратегия сортировки: сортировка пузырьком
class BubbleSort(SortingStrategy):
    def sort(self, data):
        print("Сортировка пузырьком")
        return sorted(data)  # Здесь используется встроенная сортировка Python для простоты


# Конкретная стратегия сортировки: быстрая сортировка
class QuickSort(SortingStrategy):
    def sort(self, data):
        print("Быстрая сортировка")
        return sorted(data)  # Здесь также используется встроенная сортировка Python


# Контекст, который использует стратегию сортировки
class Sorter:
    def __init__(self, sorting_strategy):
        self.sorting_strategy = sorting_strategy

    def set_strategy(self, sorting_strategy):
        self.sorting_strategy = sorting_strategy

    def sort_data(self, data):
        return self.sorting_strategy.sort(data)


if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6]

    # Создаем объекты стратегий
    bubble_sort = BubbleSort()
    quick_sort = QuickSort()

    # Создаем контекст с начальной стратегией сортировки (сортировка пузырьком)
    sorter = Sorter(bubble_sort)

    # Выполняем сортировку
    result = sorter.sort_data(data)
    print("Результат сортировки:", result)

    # Меняем стратегию сортировки на быструю сортировку и снова выполняем сортировку
    sorter.set_strategy(quick_sort)
    result = sorter.sort_data(data)
    print("Результат сортировки:", result)
