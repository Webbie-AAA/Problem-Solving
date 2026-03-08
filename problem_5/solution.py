def move_zeros(lst):
    num_list = []
    zero_count = 0
    for num in lst:
        if num == 0:
            zero_count += 1
        else:
            num_list.append(num)
    trailing_zeros_list = num_list + [0 for i in range(zero_count)]
    return trailing_zeros_list


print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1,
                  0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
