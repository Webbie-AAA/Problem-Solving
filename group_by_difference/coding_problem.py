def list_of_nums_within_range(range_num: int, list_of_nums: list[int]) -> list[int]:
    list_of_nums_in_range = []
    if list_of_nums == []:
        return list_of_nums
    for n in list_of_nums:
        if n in range(range_num):
            list_of_nums_in_range.append(n)
    return list_of_nums_in_range


if __name__ == "__main__":
    # assert {expected output} == {function_call(with inputs)}
    print(list_of_nums_within_range(
        2, [5, 5, 30, 80, 102, 31, 32, 1]))
