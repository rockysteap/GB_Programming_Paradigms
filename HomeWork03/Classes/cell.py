from .player import Player


class Cell:
    def __init__(self):
        self.__state = None

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state: str):
        if state in ('x', 'o'):
            self.__state = state
        else:
            raise ValueError('Состояние ячейки можно сменить на \'x\' или на \'o\'')
