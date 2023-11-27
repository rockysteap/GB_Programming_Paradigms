"""
    Декораторы
"""

# Абстрактный класс компонента, представляющий базовый объект
class Component:
    def operation(self):
        pass


# Конкретный компонент, представляющий базовый объект
class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent: базовая операция"


# Абстрактный класс декоратора, который расширяет функциональность компонента
class Decorator(Component):
    def __init__(self, component):
        self._component = component

    def operation(self):
        return self._component.operation()


# Конкретные декораторы, которые добавляют дополнительное поведение
class ConcreteDecoratorA(Decorator):
    def operation(self):
        return f"ConcreteDecoratorA: предварительная операция A\n{super().operation()}\nConcreteDecoratorA: дополнительная операция A"


class ConcreteDecoratorB(Decorator):
    def operation(self):
        return f"ConcreteDecoratorB: предварительная операция B\n{super().operation()}\nConcreteDecoratorB: другая дополнительная операция B"


if __name__ == "__main__":
    # Создаем базовый объект
    simple = ConcreteComponent()
    print("Client: Я получил простой компонент:")
    print(simple.operation())

    # Создаем декораторы и оборачиваем базовый объект в них
    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)

    print("\nClient: Теперь у меня есть декорированный компонент:")
    print(decorator2.operation())
