"""
    Паттерн Снимок (Memento)
"""

# Класс, представляющий оригинальный объект, состояние которого мы хотим сохранить
class Originator:
    def __init__(self):
        self._state = ""

    def set_state(self, state):
        print(f"Originator: Устанавливаю состояние на {state}")
        self._state = state

    def save_state_to_memento(self):
        print("Originator: Сохраняю состояние в Memento")
        return Memento(self._state)

    def restore_state_from_memento(self, memento):
        print("Originator: Восстанавливаю состояние из Memento")
        self._state = memento.get_state()

    def show_state(self):
        print(f"Originator: Текущее состояние - {self._state}")


# Класс, представляющий объект Memento для сохранения состояния Originator
class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


# Класс, представляющий объект Caretaker, который управляет сохранением и восстановлением состояния
class Caretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        print("Caretaker: Добавляю состояние в историю")
        self._mementos.append(memento)

    def get_memento(self, index):
        print("Caretaker: Получаю состояние из истории")
        return self._mementos[index]


if __name__ == "__main__":
    # Создаем объект Originator
    originator = Originator()

    # Создаем объект Caretaker
    caretaker = Caretaker()

    # Устанавливаем состояние Originator и сохраняем его
    originator.set_state("Состояние 1")
    caretaker.add_memento(originator.save_state_to_memento())

    # Устанавливаем новое состояние и снова сохраняем его
    originator.set_state("Состояние 2")
    caretaker.add_memento(originator.save_state_to_memento())

    # Восстанавливаем первое состояние и отображаем его
    originator.restore_state_from_memento(caretaker.get_memento(0))
    originator.show_state()

    # Восстанавливаем второе состояние и отображаем его
    originator.restore_state_from_memento(caretaker.get_memento(1))
    originator.show_state()
