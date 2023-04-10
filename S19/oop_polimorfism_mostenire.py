class Shape:

    def __init__(self, color):
        print("Hello din constructor Shape")
        self.__color = color

    def set_color(self, color):
        self.__color = color

    def __str__(self) -> str:
        return f"<{__class__.__name__} color: {self.__color}>"
    """Va returna numele clasei parinte"""

    # def area(self):
    #     pass


class Square(Shape):

    def __init__(self, length, color="red"):
        super().__init__(color)
        self.__length = length
        print("Hello din constructor Square")

    def area(self):
        return self.__length ** 2


class Triangle(Shape):

    def __init__(self, base, height, color="blue"):
        super().__init__(color)
        self.__base = base
        self.__height = height
        print("Hello din constructor Triangle")

    def area(self):
        return self.__base * self.__height / 2


sq1 = Square(5)
print(sq1)
print(sq1.area())

tr1 = Triangle(3, 4, 5)
print(tr1)

shapes = [Triangle(1, 2), Triangle(2, 2), Square(3), Square(4)]
for shape in shapes:
    print(shape.area())
