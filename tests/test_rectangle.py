import pytest

import src.shapes as shapes

# when using functions, instead of setup operations you use fixtures


@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10, 20)


def test_area(my_rectangle):
    assert my_rectangle.area() == 10 * 20


def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == (10 + 20) * 2
