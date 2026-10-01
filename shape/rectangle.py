from shape.shape import Shape


class Rectangle(Shape):
    def __init__(self, color: str, length: float, width: float):
        super().__init__(color)

        if length <= 0:
            raise ValueError("length must be a value greater than zero")

        if width <= 0:
            raise ValueError("width must be a value greater than zero")

        self.__length = length
        self.__width = width

    @property
    def area(self) -> float:
        return self.__length * self.__width

    def get_perimeter(self) -> float:
        return 2 * (self.__length + self.__width)

    def __str__(self) -> str:
        return (
            f"{super().__str__()}\n"
            f"This rectangle has a length of {self.__length}cm "
            f"and a width of {self.__width}cm."
        )