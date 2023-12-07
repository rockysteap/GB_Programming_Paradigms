# Паттерн 'Заместитель'
# Интерфейс Subject, который определяет общие методы для реального объекта и заместителя
class Subject:
    def request(self):
        pass


# Реальный объект, который выполняет определенные действия
class RealSubject(Subject):
    def request(self):
        print("RealSubject: Выполнение запроса")


# Заместитель, который контролирует доступ к реальному объекту
class Proxy(Subject):
    def __init__(self):
        self._real_subject = None

    def request(self):
        if self._real_subject is None:
            # Если реальный объект еще не создан, создаем его
            self._real_subject = RealSubject()
        print("Proxy: Контролирование доступа к RealSubject.")
        self._real_subject.request()


# Клиентский код
def client_code(subject):
    # Выполняем запрос через переданный объект
    subject.request()


if __name__ == "__main__":
    print("Client: Выполнение запроса через реальный объект:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("\nClient: Выполнение запроса через заместитель:")
    proxy = Proxy()
    client_code(proxy)
