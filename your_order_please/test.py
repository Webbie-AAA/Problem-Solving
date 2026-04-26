from main import order_str_by_num


def test_example_one():
    assert order_str_by_num("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est"


def test_example_two():
    assert order_str_by_num(
        "4of Fo1r pe6ople g3ood th5e the2") == "Fo1r the2 g3ood 4of th5e pe6ople"


def test_empty_string():
    assert order_str_by_num("") == ""


def test_single_word():
    assert order_str_by_num("word1") == "word1"


def test_two_words_reversed():
    assert order_str_by_num("world2 hello1") == "hello1 world2"


def test_all_numbers_one_to_nine():
    assert order_str_by_num(
        "n9 e5 o1 t2 h8 r3 f4 s7 x6") == "o1 t2 r3 f4 e5 x6 s7 h8 n9"


def test_number_positions_varied():
    assert order_str_by_num("3middle end2 1start") == "1start end2 3middle"
