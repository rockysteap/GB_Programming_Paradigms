# Паттерн 'Легковес'
# Класс, представляющий легковес (объект, который разделяется)
class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def render(self, x, y):
        # Представим здесь рендеринг дерева на экране
        print(f"Рисуем дерево {self.name} цвета {self.color} с текстурой {self.texture} на координатах ({x}, {y})")


# Класс, представляющий дерево
class Tree:
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def render(self):
        self.tree_type.render(self.x, self.y)


# Фабрика для создания легковесов (TreeType)
class TreeTypeFactory:
    _tree_types = { }

    @staticmethod
    def get_tree_type(name, color, texture):
        if name not in TreeTypeFactory._tree_types:
            # Если тип дерева не существует, создаем новый и сохраняем его
            TreeTypeFactory._tree_types[name] = TreeType(name, color, texture)
        return TreeTypeFactory._tree_types[name]


if __name__ == "__main__":
    # Создаем фабрику для создания легковесов (TreeType)
    factory = TreeTypeFactory()

    # Создаем деревья с использованием легковесов
    tree1 = Tree(1, 2, factory.get_tree_type("Ель", "зеленый", "шишки"))
    tree2 = Tree(3, 4, factory.get_tree_type("Береза", "белый", "гладкая кора"))
    tree3 = Tree(5, 6, factory.get_tree_type("Ель", "зеленый", "шишки"))

    # Рендерим деревья
    tree1.render()
    tree2.render()
    tree3.render()
