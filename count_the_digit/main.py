def is_there_digit(n: int, d: int) -> int:
    squared_nums = ''.join([str(i**2) for i in range(0, n+1)])
    return sum(1 for nums in squared_nums if str(d) in nums)
    ...


print(is_there_digit(25, 1))

# TODO: COULD SIMPLY FURTHER BY USING THE .COUNT() METHOD.
