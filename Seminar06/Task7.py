# Поведенческий паттерн 'Команда'
from abc import ABC, abstractmethod


# Абстрактный класс Command
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# Конкретная команда: включение света
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


# Конкретная команда: выключение света
class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()


# Класс, представляющий свет
class Light:
    def turn_on(self):
        print("Свет включен")

    def turn_off(self):
        print("Свет выключен")


# Класс, представляющий пульт управления
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command is not None:
            self.command.execute()


if __name__ == "__main__":
    # Создаем объект света
    light = Light()

    # Создаем команды для включения и выключения света
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    # Создаем пульт управления и настраиваем его кнопки
    remote = RemoteControl()
    remote.set_command(light_on)

    # Пользователь нажимает кнопку на пульте
    remote.press_button()

    # Меняем команду на выключение и снова нажимаем кнопку
    remote.set_command(light_off)
    remote.press_button()
