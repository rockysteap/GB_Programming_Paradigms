"""
    Паттерн Фабрика
"""

from abc import ABC, abstractmethod


# Абстрактный класс Creator (Создатель)
class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):
        # Вызываем фабричный метод для создания объекта
        product = self.factory_method()
        result = f"Creator: {product.operation()}"
        return result


# Конкретные классы создателей
class ConcreteCreator1(Creator):
    def factory_method(self):
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self):
        return ConcreteProduct2()


# Абстрактный класс Product (Продукт)
class Product(ABC):
    @abstractmethod
    def operation(self):
        pass


# Конкретные классы продуктов
class ConcreteProduct1(Product):
    def operation(self):
        return "ConcreteProduct1"


class ConcreteProduct2(Product):
    def operation(self):
        return "ConcreteProduct2"


# Пример использования
def client_code(creator):
    print(f"Client: {creator.some_operation()}")


if __name__ == "__main__":
    print("App: запущен с ConcreteCreator1.")
    client_code(ConcreteCreator1())

    print("\nApp: запущен с ConcreteCreator2.")
    client_code(ConcreteCreator2())
