def get_multiplicative_persistence(num: int) -> int:
    count = 0
    while len(str(num)) != 1:
        count += 1
        num = str(number_multiplies_itself(num))
    return count

    ...


def number_multiplies_itself(num: int) -> int:
    num_list = list(str(num))
    multiplied = 1
    for i in num_list:
        multiplied *= int(i)
    return multiplied

# TODO: Is there an easier way to do the multiplicative element of the problem?


if __name__ == '__main__':
    print(get_multiplicative_persistence(999))
