# Поведенческий паттерн 'Наблюдатель'
# Интерфейс для наблюдателей
class Observer:
    def update(self, temperature):
        pass


# Конкретный наблюдатель
class WeatherObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, temperature):
        print(f"{self.name}: Температура изменилась на {temperature} градусов")


# Субъект (издатель), который генерирует события
class WeatherStation:
    def __init__(self):
        self.observers = []
        self.temperature = 0

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def set_temperature(self, temperature):
        self.temperature = temperature
        self.notify_observers()

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature)


if __name__ == "__main__":
    # Создаем объект субъекта (погодной станции)
    weather_station = WeatherStation()

    # Создаем наблюдателей
    observer1 = WeatherObserver("Наблюдатель 1")
    observer2 = WeatherObserver("Наблюдатель 2")

    # Регистрируем наблюдателей
    weather_station.add_observer(observer1)
    weather_station.add_observer(observer2)

    # Устанавливаем новую температуру, которая автоматически уведомит наблюдателей
    weather_station.set_temperature(25.5)
