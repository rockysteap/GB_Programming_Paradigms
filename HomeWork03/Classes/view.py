from os import name as sys_name

from os import system as sys_cmd


class View:
    _counter = 0

    def __new__(cls, *args, **kwargs):
        raise NotImplementedError('Сервисный класс - экземпляры не создаются')

    @classmethod
    def clear(cls):
        if sys_name == 'nt':
            sys_cmd('cls')
        else:
            sys_cmd('clear')

    @classmethod
    def show(cls, f: list, p: str, first_show=False):
        cls.clear()
        cls.__show_info_upper(p, first_show)
        cls.__show_field(f)

    @classmethod
    def __show_info_upper(cls, p: str, first_show=False):
        print(f'''
 Крестики-нолики             {f'Начинает {p}' if first_show else f'Ход {p}'}
 ---------------------------------------
 Игровое поле                Управление''')

    @classmethod
    def __show_field(cls, f: list):
        print()
        print(f'  {f[0]} | {f[1]} | {f[2]}                  7 | 8 | 9')
        print(' ---+---+---                ---+---+---')
        print(f'  {f[3]} | {f[4]} | {f[5]}                  4 | 5 | 6')
        print(' ---+---+---                ---+---+---       (q)uit')
        print(f'  {f[6]} | {f[7]} | {f[8]}                  1 | 2 | 3        (r)estart')

        print()
        cls._counter += 1

    @classmethod
    def pycharm_info(cls):
        print('''\n Если запуск производится из PyCharm.\n
 Для корректной очистки экрана необходимо включить эмуляцию терминала:
  
  -> Нажать на кнопку с тремя точками (наверху, радом с run и debug)
  -> Выбрать Edit..
  -> В новом окне 'Run/Debug Configurations' нажать Alt + M
  -> В выпадающем меню выбрать 'Emulate terminal in output console'
  
  Описание основано на PyCharm 2023.2.5 (Community Edition)
        ''')
        input(' Для продолжения нажмите Enter...')
