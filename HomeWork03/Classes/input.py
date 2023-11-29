import keyboard


class Input:
    def __new__(cls, *args, **kwargs):
        raise NotImplementedError('Сервисный класс - экземпляры не создаются')

    @classmethod
    def get_input(cls, possible_inputs_list: list) -> str:
        if 'й' not in possible_inputs_list or 'к' not in possible_inputs_list:
            possible_inputs_list.extend(['й', 'к'])
        while True:
            k = keyboard.read_key()
            if k in possible_inputs_list:
                return k

    @classmethod
    def process_user_input(cls, user_input: str):
        c = user_input
        match c:
            case c if c.lower() in ('q', 'й'):
                print('\nЗавершение работы...')
                exit(0)
            case c if c.lower() in ('r', 'к'):
                return 'r'
            case c if c in [str(a) for a in range(1, 10)]:
                return c
