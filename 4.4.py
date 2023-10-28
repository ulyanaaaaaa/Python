class Rectangle:
    # Статическое поле класса
    total_rectangles = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        # Увеличиваем значение статического поля при создании нового экземпляра класса
        Rectangle.total_rectangles += 1

    # Метод экземпляра класса
    def calculate_area(self):
        return self.width * self.height

    # Статический метод
    @staticmethod
    def is_square(rectangle):
        return rectangle.width == rectangle.height

    # Метод класса
    @classmethod
    def print_total_rectangles(cls):
        print(f"Total number of rectangles created: {cls.total_rectangles}")


# Создание экземпляров класса
rectangle1 = Rectangle(5, 10)
rectangle2 = Rectangle(3, 3)
rectangle3 = Rectangle(7, 4)

# Вызов методов экземпляра класса
print("Area of rectangle 1:", rectangle1.calculate_area())
print("Area of rectangle 2:", rectangle2.calculate_area())
print("Area of rectangle 3:", rectangle3.calculate_area())

# Вызов статического метода
print("Is rectangle 1 a square?", Rectangle.is_square(rectangle1))
print("Is rectangle 2 a square?", Rectangle.is_square(rectangle2))
print("Is rectangle 3 a square?", Rectangle.is_square(rectangle3))

# Вызов метода класса
Rectangle.print_total_rectangles()