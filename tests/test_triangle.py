import pytest

from shape.triangle import Triangle


def test_init_color_blank():
    with pytest.raises(ValueError, match="color cannot be blank"):
        Triangle("   ", 5, 6, 7)


def test_init_side_1_less_than_zero():
    with pytest.raises(
        ValueError,
        match="side_1 must be a value greater than zero"
    ):
        Triangle("red", -1, 6, 7)


def test_init_side_2_less_than_zero():
    with pytest.raises(
        ValueError,
        match="side_2 must be a value greater than zero"
    ):
        Triangle("red", 5, -1, 7)


def test_init_side_3_less_than_zero():
    with pytest.raises(
        ValueError,
        match="side_3 must be a value greater than zero"
    ):
        Triangle("red", 5, 6, -1)


def test_init_sides_do_not_satisfy_triangle_inequality_theorem():
    with pytest.raises(
        ValueError,
        match="The sides do not satisfy the Triangle Inequality Theorem"
    ):
        Triangle("red", 1, 2, 3)


def test_init_new_instance():
    triangle = Triangle("red", 5, 6, 7)

    assert triangle._Shape__color == "red"
    assert triangle._Triangle__side_1 == 5
    assert triangle._Triangle__side_2 == 6
    assert triangle._Triangle__side_3 == 7


def test_color_property():
    triangle = Triangle("red", 5, 6, 7)

    assert triangle.color == "red"


def test_area_property():
    triangle = Triangle("red", 5, 6, 7)

    assert triangle.area == pytest.approx(14.696938456699069)


def test_get_perimeter():
    triangle = Triangle("red", 5, 6, 7)

    assert triangle.get_perimeter() == 18


def test_str():
    triangle = Triangle("red", 5, 6, 7)

    expected = (
        "The shape color is red.\n"
        "This triangle has three sides with lengths of "
        "5, 6, and 7 centimeters."
    )

    assert str(triangle) == expected