letters = list("ashdjsgfbdfhnxcbsajkdjse")
print(letters.count('e'))

letters = set(letters)
print([l for l in letters])


def letters_cleaned(x: str) -> str:
    """Given a string of letters them, returns them all lowercase without whitespace"""
    return x.lower().replace(' ', '')


def count_letters_in_dict(letters: str) -> int:
    """Given a string of letters, returns a dictionary containing each 
    individual char and frequency of occurrence"""
    char_count = {}
    if len(letters) > 0:
        letters = letters_cleaned(letters)
        letters_set = set(letters)
        for x in letters_set:
            char_count[x] = letters.count(x)
        return char_count
    return char_count

    ...


print(count_letters_in_dict("a a"))


# Someone's superior solution:
def count(string):

    return {i: string.count(i) for i in string}
