def valid_palindrome(s: str) -> bool:
    if s == s[::-1]:
        return True
    for char in range(len(s)):
        result = s[:char]+s[char+1:]
        if result == result[::-1]:
            return True
    return False

    ...


def instant_palindrome(s):
    if s == s[::-1]:
        return True
    return False


valid_palindrome("hello")
