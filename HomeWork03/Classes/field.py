from typing import List

from .cell import Cell


class Field:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        Field.__instance = None

    def __init__(self):
        """
        Индексы ячеек [0, 9)
        0 1 2
        3 4 5
        6 7 8
        """
        self.__checking_char = None
        self.__field = [Cell() for _ in range(9)]

    def __check_symbol(self, char) -> bool:
        return char == self.__checking_char

    def check_win_conditions(self, s) -> bool:
        """
        Проверка выигрыша срезами.
        Ряды:       [:3] [3:6] [6:]
        Колонки:    [::3] [1::3] [2::3]
        Диагонали:  [::4] [2::2]
        :param s: Символ для проверки выигрышной комбинации.
        :return: Булево значение.
        """
        self.__checking_char = s
        c = self.__check_symbol
        f = self.get_field()
        win = any([all(map(c, f[:3])), all(map(c, f[3:6])), all(map(c, f[6:])),
                   all(map(c, f[::3])), all(map(c, f[1::3])), all(map(c, f[2::3])),
                   all(map(c, f[::4])), all(map(c, f[2:8:2])) ])
        self.__checking_char = None
        return win

    def free_cells(self) -> bool:
        """
        Проверка поля на наличие свободных ячеек.
        :return: Булево значение.
        """
        return not any(map(lambda cell: cell.state, self.__field))

    def get_field(self):
        return [c.state if c.state else ' ' for c in self.__field]

    def set_state_by_cell_index(self, indx: int, state: str):
        self.__field[indx].state = state
