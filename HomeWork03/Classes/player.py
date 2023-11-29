from random import choice


class Player:
    def __init__(self, mark):
        self.__mark = mark

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, value):
        if value in ('x', 'o'):
            self.__mark = value
        else:
            raise ValueError('Игрок может быть или \'x\' или \'o\'')

    @classmethod
    def get_first(cls):
        players = ('x', 'o')
        return choice(players)
