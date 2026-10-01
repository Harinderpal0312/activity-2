from shape.shape import Shape


class Triangle(Shape):
    def __init__(self, color: str, side_1: float, side_2: float, side_3: float):
        super().__init__(color)

        if side_1 <= 0:
            raise ValueError("side_1 must be a value greater than zero")

        if side_2 <= 0:
            raise ValueError("side_2 must be a value greater than zero")

        if side_3 <= 0:
            raise ValueError("side_3 must be a value greater than zero")

        if (
            side_1 + side_2 <= side_3
            or side_1 + side_3 <= side_2
            or side_2 + side_3 <= side_1
        ):
            raise ValueError(
                "The sides do not satisfy the Triangle Inequality Theorem"
            )

        self.__side_1 = side_1
        self.__side_2 = side_2
        self.__side_3 = side_3

    @property
    def area(self) -> float:
        sp = self.get_perimeter() / 2
        return (
            sp
            * (sp - self.__side_1)
            * (sp - self.__side_2)
            * (sp - self.__side_3)
        ) ** 0.5

    def get_perimeter(self) -> float:
        return self.__side_1 + self.__side_2 + self.__side_3

    def __str__(self) -> str:
        return (
            f"{super().__str__()}\n"
            f"This triangle has three sides with lengths of "
            f"{self.__side_1}, {self.__side_2}, and "
            f"{self.__side_3} centimeters."
        )