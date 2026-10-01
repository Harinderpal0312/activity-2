from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color: str):
        color = color.strip()

        if color == "":
            raise ValueError("color cannot be blank")

        self.__color = color

    @property
    def color(self) -> str:
        return self.__color

    @property
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def get_perimeter(self) -> float:
        pass

    def __str__(self) -> str:
        return f"The shape color is {self.__color}."