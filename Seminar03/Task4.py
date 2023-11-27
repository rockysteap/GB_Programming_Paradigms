"""
    Паттерн Адаптер
"""

# Класс, который представляет интерфейс, несовместимый с ожидаемым клиентом
class IncompatibleComponent:
    def specific_request(self):
        return "Specific Request"


# Интерфейс, который ожидает клиент
class Target:
    def request(self):
        pass


# Адаптер, который адаптирует IncompatibleComponent к Target
class Adapter(Target):
    def __init__(self, component):
        self._component = component

    def request(self):
        return f"Adapter: {self._component.specific_request()}"


# Клиентский код, который ожидает работать с Target, но использует Adapter
def client_code(target):
    result = target.request()
    return result


if __name__ == "__main__":
    component = IncompatibleComponent()
    adapter = Adapter(component)

    result = client_code(adapter)
    print(result)
