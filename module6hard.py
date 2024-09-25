import math

class Figure:
    sides_count = 0

    def __init__(self, sides: list, color: list, filed=False):
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = sides
        self.__color = color
        self.filed = filed

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            print('Цвет изменён')
        else:
            print('Неподходящее значение цвета для изменения')

    def __is_valid_sides(self, *args):
        if len(args) != self.sides_count:
            return False
        for i in args:
            if not isinstance(i, int) or i <= 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            print('Неверное количество сторон')
            return
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            print('Неверные значения сторон')


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: list, radius):
        super().__init__([2 * math.pi * radius], color, True)
        self.__radius = radius

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, sides: list, color: list, filed: bool):
        super().__init__(sides, color, filed)

    def get_square(self):
        sides = self.get_sides()  # Используем метод get_sides()
        p = 0.5 * sum(sides)
        return pow((p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])), 0.5)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: list, side, filed=False):
        super().__init__([side] * 12, color, filed)
        self.__side = side

    def get_volume(self):
        return self.__side ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
