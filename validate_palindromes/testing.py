# pylint: skip-file

import pytest

from coding_problem import valid_palindrome


def test_basic_test_1():
    # Already a palindrome
    assert valid_palindrome("aba") == True


def test_basic_test_2():
    # Can remove 'c' or 'b'
    assert valid_palindrome("abca") == True


def test_basic_test_3():
    # Cannot form palindrome
    assert valid_palindrome("abc") == False


def test_basic_test_4():
    # Already a palindrome
    assert valid_palindrome("racecar") == True


def test_basic_test_5():
    # Can remove one 'e'
    assert valid_palindrome("deeee") == True


def test_single_char():
    assert valid_palindrome("a") == True


def test_two_chars_same():
    assert valid_palindrome("aa") == True


def test_two_chars_different():
    assert valid_palindrome("ab") == True


def test_all_same_chars():
    assert valid_palindrome("aaaa") == True


def test_empty_after_one_removal():
    assert valid_palindrome("ab") == True


def test_long_palindrome():
    assert valid_palindrome("racecar") == True


def test_remove_from_start():
    assert valid_palindrome("xaba") == True


def test_remove_from_end():
    assert valid_palindrome("abax") == True


def test_remove_from_middle():
    assert valid_palindrome("abxba") == True


@pytest.mark.parametrize(
    "s,is_valid",
    [
        # Simple palindromes (no removal needed)
        ("a", True),
        ("aa", True),
        ("aba", True),
        ("abba", True),
        ("racecar", True),
        ("noon", True),
        # Remove one char to make palindrome
        ("abca", True),  # Remove 'c' -> "aba"
        ("deeee", True),  # Remove one 'e'
        (
            "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga",
            True,
        ),
        ("ebcbbececabbacecbbcbe", True),
        ("abc", False),
        ("abcdef", False),
        ("abcd", False),
        # Edge cases with removal
        (
            "abac",
            True,
        ),  # Remove second 'a' -> "abc" is not palindrome, but remove 'c' -> "aba"
        # Two character strings
        ("ab", True),
        ("ba", True),
        # Tricky cases
        ("abcba", True),  # Already palindrome
        ("abcdba", True),  # Remove 'd' or 'c'
        ("raceacar", True),  # Remove 'a' in middle
        ("raceecar", True),  # Remove an 'e'
        # Long strings that need removal
        (
            "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga",
            True,
        ),
        # Cannot form palindrome
        ("abcdefg", False),
        ("abcdefghijklmn", False),
        ("abcda", False),
        # Repeated characters
        ("aaaaaa", True),
        ("aaabaa", True),
        ("aabaaa", True),
        # More complex cases
        (
            "madame",
            True,
        ),  # Remove second 'a' -> "madme" not palindrome, but remove 'e' -> "madam"
        ("abcdedcba", True),  # Already palindrome
        ("abcddcba", True),  # Already palindrome
        ("abcdeedcba", True),  # Already palindrome
        # Real challenging cases
        ("ebcbbececabbacecbbcbe", True),
        ("acxcybycxcxa", True),
        (
            "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga",
            True,
        ),
        # False cases
        ("abcdef", False),
        ("abccde", False),
        ("abcdefghij", False),
    ],
)
def test_random_test_cases(s, is_valid):
    assert valid_palindrome(s) == is_valid


def test_three_char_palindrome():
    # Three characters - remove middle
    assert valid_palindrome("aba") == True
    assert valid_palindrome("abc") == False


def test_alternating_chars():
    # Alternating pattern
    assert valid_palindrome("abab") == True
