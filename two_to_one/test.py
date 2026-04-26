from main import two_to_one


def test_return_ordered_distinct_longest_str():
    # Arrange
    a = "xyaabbbccccdefww"
    b = "xxxxyyyyabklmopq"
    output = "abcdefklmopqwxy"
    # Act
    result = two_to_one(a, b)
    # Assert
    assert result == output
    ...
