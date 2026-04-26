def order_str_by_num(unordered_sen: str) -> str:
    ordered_sen = ''
    sen_list = unordered_sen.split(' ')
    for i in range(1, len(sen_list)+1):
        ordered_sen += ' ' + ''.join(word for word in sen_list if str(i)
                                     in word)
    return ordered_sen


print(order_str_by_num("is2 Thi1s T4est 3a"))
