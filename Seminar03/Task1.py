"""
    Паттерн Синглтон
"""

class Singleton:
    _instance = None  # Приватное поле для хранения единственного экземпляра класса

    def __new__(cls):
        if cls._instance is None:
            # Если экземпляр еще не создан, создаем его
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.value = None  # Пример поля для хранения данных в одиночке
        return cls._instance


# Создаем два объекта, но они будут одним и тем же экземпляром
singleton1 = Singleton()
singleton2 = Singleton()

# Устанавливаем значение для singleton1
singleton1.value = "Hello, Singleton!"

# Выводим значение из singleton2, и оно будет таким же, как в singleton1
print(singleton2.value)  # Вывод: "Hello, Singleton!"
