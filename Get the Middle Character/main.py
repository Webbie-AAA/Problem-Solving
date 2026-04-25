def get_middle_chars(chars: str) -> str:
    len_chars = len(chars)
    if len_chars > 1:
        if len_chars % 2 == 0:
            return chars[(len_chars//2)-1] + chars[(len_chars//2)]
        else:
            return chars[len_chars//2]
    return chars
    ...
