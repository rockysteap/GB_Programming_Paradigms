from .field import Field
from .input import Input
from .player import Player
from .view import View


class Game:
    def __init__(self):
        """
        __f                 поле из девяти ячеек
        __p                 текущий игрок (тот, чей ход, 'x' или 'o')
        __p1, __p2          игроки 1 и 2
        __moves             разрешенный ввод (срабатывание на нажатие)
        __num_to_cell_dict  соответствие ввода и индексов ячеек
        """
        self.__f = self.__p = self.__p1 = self.__p2 = None
        self.__moves = self.__num_to_cell_dict = None

    def start(self):
        self.__preps()
        self.__game_loop()

    def __preps(self):
        self.__init_moves()
        self.__f = Field()
        self.__p = self.__p1 = Player(Player.get_first())
        self.__p2 = Player('x' if self.__p1.mark == 'o' else 'o')

    def __game_loop(self):
        f, p1, p2 = self.__f, self.__p1, self.__p2
        p = self.__p  # текущий игрок
        m = self.__moves  # разрешенный ввод в виде списка
        won = winner = None
        View.show(f.get_field(), p.mark, True)
        # -------------------------------------------------------
        while True:
            m_out = ', '.join(m)  # разрешенный ввод в виде строки
            print(f'Ожидание ввода -> {m_out}', end=' ')
            k = Input.process_user_input(Input.get_input(m))
            if k == 'r':
                break
            # Изменим состояние ячейки на символ текущего игрока
            f.set_state_by_cell_index(self.__get_cell_index_by_input(k), p.mark)
            # Проверим выигрышные комбинации
            if f.check_win_conditions(p.mark):
                won = True
                winner = p.mark
            # Сократим список предлагаемого ввода
            m.remove(k)
            # Сменим игрока
            p = self.__change_player()
            # Отрисуем интерфейс
            View.show(f.get_field(), p.mark)
            # Остановим и сообщим в случае выигрыша
            if won:
                print(f'\nИгрок \'{winner}\' победил! Продолжить? (q,r)')
                Input.process_user_input(Input.get_input(m))
                break

    def __change_player(self) -> Player:
        self.__p = self.__p1 if self.__p == self.__p2 else self.__p2
        return self.__p

    def __init_moves(self):
        self.__moves = [str(a) for a in range(1, 10)]
        self.__moves.extend(['q', 'r'])

    def __get_cell_index_by_input(self, user_input: str) -> int:
        # словарь соответствия клавиатурного ввода с индексами ячеек поля
        if not self.__num_to_cell_dict:
            self.__init_num_to_cell_dict()
        return self.__num_to_cell_dict[user_input]

    def __init_num_to_cell_dict(self):
        numpad_lst = [7, 8, 9, 4, 5, 6, 1, 2, 3]
        indices_lst = [i for i in range(9)]
        self.__num_to_cell_dict = { str(i[0]): i[1] for i in zip(numpad_lst, indices_lst) }
