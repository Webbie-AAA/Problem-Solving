def order_str_by_num(unordered_sen: str) -> str:
    """Given a string with consecutive embedded numbers, this string
    organises the str according to the numbers ordered."""
    ordered_sen = ''
    sen_list = unordered_sen.split(' ')
    for i in range(1, len(sen_list)+1):
        ordered_sen += ' ' + ''.join(word for word in sen_list if str(i)
                                     in word)
    return ordered_sen.strip()
