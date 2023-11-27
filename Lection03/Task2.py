import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = None
        self.perimeter = None
        self.diagonal = None

    def __add__(self, other):
        return self.area + other.area

    def __eq__(self, other):
        return self.area == other.area

    def get_area(self):
        # также добавим локальный атрибут
        self.area = self.width * self.height
        return self.area

    def get_perimeter(self):
        # также добавим локальный атрибут
        self.perimeter = (self.width + self.height) * 2
        return self.perimeter

    def get_diagonal(self):
        # также добавим локальный атрибут
        self.diagonal = (self.width * self.width + self.height * self.height) ** 0.5
        return self.diagonal

    def get_diagonal_angles(self):
        """
        Рассчитывает и возвращает два угла прямоугольного треугольника,
        гипотенуза которого образована путем диагонального деления прямоугольника.
        :return: Кортеж из двух углов.
        """
        if not hasattr(self, 'diagonal'):
            self.get_diagonal()
        cos_between_diag_and_height = self.height / self.diagonal
        angle_between_diag_and_height = math.degrees(math.acos(cos_between_diag_and_height))
        angle1 = 180 - (2 * angle_between_diag_and_height)
        angle2 = (360 - 2 * angle1) / 2
        assert angle1 + angle2 == 180
        return angle1, angle2


print(type(Rectangle))  # class type - мета-класс в python
r = Rectangle(12, 16)

r.get_area()
r.get_perimeter()
r.get_diagonal()
print(r.get_diagonal_angles())
print(r.__dict__)

r2 = Rectangle(16, 12)
r2.get_area()
r3 = r + r2
print(r3)  # 392
print(r == r2)  # True
