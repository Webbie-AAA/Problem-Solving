def create_phone_number(n):
    n = ["" + str(num) for num in n]
    phone_num = ''.join(n).replace(",", "")
    return f"({phone_num[:3]}) {phone_num[3:6]}-{phone_num[6:]}"
