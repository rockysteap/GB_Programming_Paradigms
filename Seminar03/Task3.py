"""
    Паттерн Строитель
"""

# Класс продукта, который мы будем строить пошагово
class Product:
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def list_parts(self):
        return ", ".join(self.parts)


# Интерфейс строителя (Builder)
class Builder:
    def build_part_a(self):
        pass

    def build_part_b(self):
        pass

    def get_result(self):
        pass


# Конкретный строитель (ConcreteBuilder)
class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add_part("Part A")

    def build_part_b(self):
        self.product.add_part("Part B")

    def get_result(self):
        return self.product


# Директор (Director), который управляет строителем
class Director:
    def __init__(self, builder):
        self.builder = builder

    def build_minimal_product(self):
        self.builder.build_part_a()

    def build_full_product(self):
        self.builder.build_part_a()
        self.builder.build_part_b()


if __name__ == "__main__":
    # Создаем конкретного строителя
    builder = ConcreteBuilder()

    # Создаем директора, передавая ему строителя
    director = Director(builder)

    # Строим минимальный продукт
    director.build_minimal_product()
    minimal_product = builder.get_result()
    print(f"Minimal Product Parts: {minimal_product.list_parts()}")

    # Строим полный продукт
    director.build_full_product()
    full_product = builder.get_result()
    print(f"Full Product Parts: {full_product.list_parts()}")
