import pytest

from shape.rectangle import Rectangle


def test_init_color_blank():
    with pytest.raises(ValueError, match="color cannot be blank"):
        Rectangle("   ", 5, 6)


def test_init_length_less_than_zero():
    with pytest.raises(
        ValueError,
        match="length must be a value greater than zero"
    ):
        Rectangle("red", -1, 6)


def test_init_width_less_than_zero():
    with pytest.raises(
        ValueError,
        match="width must be a value greater than zero"
    ):
        Rectangle("red", 5, -1)


def test_init_new_instance():
    rectangle = Rectangle("red", 5, 6)

    assert rectangle._Shape__color == "red"
    assert rectangle._Rectangle__length == 5
    assert rectangle._Rectangle__width == 6


def test_color_property():
    rectangle = Rectangle("red", 5, 6)

    assert rectangle.color == "red"


def test_area_property():
    rectangle = Rectangle("red", 5, 6)

    assert rectangle.area == 30


def test_get_perimeter():
    rectangle = Rectangle("red", 5, 6)

    assert rectangle.get_perimeter() == 22


def test_str():
    rectangle = Rectangle("red", 5, 6)

    expected = (
        "The shape color is red.\n"
        "This rectangle has a length of 5cm and a width of 6cm."
    )

    assert str(rectangle) == expected