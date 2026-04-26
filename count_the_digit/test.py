from main import is_there_digit


def test_is_there_digit():
    # Arrange
    n = 10
    d = 1
    output = 4
    # Act
    result = is_there_digit(n, d)
    # Assert
    assert result == output
    ...
