# Ввод текста з клави
# Букви та цифри, переходять в наступні
# Має працювати все разом
# Після кінця має йти в початок
#

input_var = input("Enter value: ")
crypt_index = 1
result_list = []

latin_symbols_lower = "abcdefghijklmnopqrstuvwxyz"
latin_symbols_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ua_symbols_lower = "абвгґдеєжзийїклмнопрстуфхцчшщьюя"
ua_symbols_upper = "АБВГҐДЕЄЖЗИЙЇКЛМНОПРСТУФХЦЧШЩЬЮЯ"
digits_symbols = "0123456789"

for symb in input_var:

    if symb in latin_symbols_lower:
        new_index = (latin_symbols_lower.index(symb) + crypt_index) % 26
        result_list.append(latin_symbols_lower[new_index])

    elif symb in latin_symbols_upper:
        new_index = (latin_symbols_upper.index(symb) + crypt_index) % len(latin_symbols_upper)
        result_list.append(latin_symbols_upper[new_index])

    elif symb in ua_symbols_lower:
        new_index = (ua_symbols_lower.index(symb) + crypt_index) % len(ua_symbols_lower)
        result_list.append(ua_symbols_lower[new_index])

    elif symb in ua_symbols_upper:
        new_index = (ua_symbols_upper.index(symb) + crypt_index) % len(ua_symbols_upper)
        result_list.append(ua_symbols_upper[new_index])

    elif symb in digits_symbols:
        new_index = (digits_symbols.index(symb) + crypt_index) % len(digits_symbols)
        result_list.append(digits_symbols[new_index])

    else:
        result_list.append(symb)


resultat = ''.join(result_list)
print(resultat.lower())