from main import get_middle_chars


def test_get_even_middle_chars():
    # Arrange
    word = "test"
    output = 'es'
    # Act
    result = get_middle_chars(word)
    # Assert
    assert result == output
    ...


def test_get_odd_middle_chars():
    # Arrange
    word = "testing"
    output = "t"
    # Act
    result = get_middle_chars(word)
    # Assert
    assert result == output
    ...


def test_get_single_chars():
    # Arrange
    word = 'A'
    output = 'A'
    # Act
    result = get_middle_chars(word)
    # Assert
    assert result == output
    ...
