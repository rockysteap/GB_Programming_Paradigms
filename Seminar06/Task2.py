# Паттерн 'Мост'
# Абстракция
class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        pass


# Реализация
class Color:
    def fill_color(self):
        pass


# Конкретная абстракция
class Circle(Shape):
    def draw(self):
        print(f"Рисуем круг {self.color} цвета")


# Конкретная абстракция
class Square(Shape):
    def draw(self):
        print(f"Рисуем квадрат {self.color} цвета")


# Конкретная реализация
class RedColor(Color):
    def fill_color(self):
        return "красным"


# Конкретная реализация
class GreenColor(Color):
    def fill_color(self):
        return "зеленым"


if __name__ == "__main__":
    # Создаем круг с красным цветом
    circle_red = Circle(RedColor())
    circle_red.draw()

    # Создаем квадрат с зеленым цветом
    square_green = Square(GreenColor())
    square_green.draw()
