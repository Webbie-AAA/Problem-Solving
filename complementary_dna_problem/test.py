import pytest
from main import return_dna_complement


def test_return_dna_complement():
    # Arrange
    dna_input = "ATTGC"
    complementary_pair = "TAACG"
    # Act
    result = return_dna_complement(dna_input)
    # Assert
    assert result == complementary_pair
    ...


def test_return_dna_complement_in_upper():
    # Arrange
    dna_input = "attgc"
    complementary_pair = "TAACG"
    # Act
    result = return_dna_complement(dna_input)
    # Assert
    assert result == complementary_pair
    ...


def test_value_error():
    with pytest.raises(ValueError, match="DNA letter must be either A, T, G, C"):
        return_dna_complement("KBG")
