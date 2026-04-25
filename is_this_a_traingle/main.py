
def is_triangle(a: int, b: int, c: int) -> bool:
    """Given a three numbers, if they form a triangle returns true else
    returns false"""
    if (a + b > c) and (b + c > a) and (c + a > b):
        return True
    return False
    ...
