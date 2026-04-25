from main import is_triangle
import pytest


def test_equilateral_tri():
    # Arrange
    output = True
    # Act
    result = is_triangle(2, 2, 2)
    # Assert
    assert result == output
    ...


def test_is_triangle():
    # Arrange
    output = True
    # Act
    result = is_triangle(1, 2, 2)
    # Assert
    assert result == output
    ...


def test_is_not_triangle():
    # Arrange
    output = False
    # Act
    result = is_triangle(1, 2, 3)
    # Assert
    assert result == output
    ...


def test_negative_values():
    # Arrange
    output = False
    # Act
    result = is_triangle(-5, 1, 3)
    # Assert
    assert result == output

# NOT NEEDED:
# def test_value_error():
#     with pytest.raises(ValueError, match="No more than 3 numbers can be entered"):
#         is_triangle(1, 2, 3, 4)
