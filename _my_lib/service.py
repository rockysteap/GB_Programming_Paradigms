from random import choice


class Service:

    @staticmethod
    def get_random_int_list(qty: int = 20, min_value: int = -100, max_value: int = 100) -> list:
        """
        Возвращает неупорядоченный список целочисленных значений.
        :param qty: Количество элементов списка.
        :param min_value: Минимальное значение выборки.
        :param max_value: Максимальное значение выборки.
        :return: Неупорядоченный список.
        """
        return [choice([x for x in range(min_value, max_value)]) for _ in range(qty)]
