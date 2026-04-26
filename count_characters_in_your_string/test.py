from main import count_letters_in_dict


def test_empty_string():
    assert count_letters_in_dict("") == {}


def test_single_character():
    assert count_letters_in_dict("a") == {"a": 1}


def test_basic_case():
    assert count_letters_in_dict("aba") == {"a": 2, "b": 1}


def test_multiple_characters():
    assert count_letters_in_dict("abcabc") == {"a": 2, "b": 2, "c": 2}


def test_case_sensitivity():
    assert count_letters_in_dict("aA") == {"a": 2}


def test_with_spaces():
    assert count_letters_in_dict("a a") == {"a": 2}


def test_with_numbers():
    assert count_letters_in_dict("112233") == {"1": 2, "2": 2, "3": 2}


def test_with_special_characters():
    assert count_letters_in_dict("!!??!") == {"!": 3, "?": 2}


def test_longer_string():
    assert count_letters_in_dict("hello world") == {
        "h": 1, "e": 1, "l": 3, "o": 2,
        "w": 1, "r": 1, "d": 1
    }
