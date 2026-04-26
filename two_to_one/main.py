letters = "avfdfgjhrfbnkeufjhiowa"
more_letters = "auwdhgsryujhgfbdjkc"
letters = set(letters + more_letters)
print(''.join(sorted(letters)))


def two_to_one(x: str, y: str) -> str:
    """takes two string, combines them and returns an ordered
    string made of distinct letters"""
    letters = set(x+y)
    return ''.join(sorted(letters))
    ...
