# while True:
#     try:
#         digit1 = float(input("Enter first number: "))
#     except ValueError:
#         print("Wrong input")
#         break
#     try:
#         digit2 = float(input("Enter second number: "))
#     except ValueError:
#         print("Wrong input")
#         break

def letters_counter(words_list):
    count = 0
    for word in words_list:
        for symbol in word:
            if symbol.isalpha():
                count += 1
    return count

def reverser():
    reverse_variable = str(input("Enter string to reverse: "))
    print(reverse_variable[::-1])

def dictionary():
    dictionary_var = []
    print("(q or exit to finish)", '\n')

    while True:

        words = input(str("Add words to dictionary: "))

        capitalized_words = words.capitalize()

        if words == "q":
            print('\n', "/////////// Finished ///////////", '\n')
            break
        elif words == "exit":
            break

        if capitalized_words in dictionary_var:
            continue
        else:
            dictionary_var.append(capitalized_words)

    sorted_words = sorted(dictionary_var)
    for word in sorted_words:
        print(word)

    counted_letters = letters_counter(sorted_words)
    print("Letters in dictionary", counted_letters)

def calculator():
    while True:

        digit1 = float(input("Enter first number: "))
        digit2 = float(input("Enter second number: "))

        print("Operators: \'+\', \'-\', \'*\', \'/\', 'skip to exit' ")
        operation = input("Enter operator: ")

        if operation == '+':
            print("Result: ", digit1 + digit2)
        elif operation == '-':
            print("Result: ", digit1 - digit2)
        elif operation == '*':
            print("Result: ", digit1 * digit2)
        elif operation == "/":
            if digit2 == 0:
                print("We cannot divide on zero")
            else:
                print("Result: ", digit1 / digit2)
        else:
            print('\n', "///////////Finished///////////")
            break

def duplicator():
    stringa = str(input("Enter string: "))
    multiplier = int(input("Enter multiplier: "))

    multiplied_str = ""

    for i in stringa:
        if i != ' ':
            multiplied_str += i * multiplier
        else:
            multiplied_str += i

    print(multiplied_str)

def caesar_crypto():
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




print("Choose variation.",
        '\n', "Enter \"cl\" for Calculator",
        '\n', "Enter \"dc\" for Dictionary",
        '\n', "Enter \"rv\" for Reverser",
        '\n', "Enter \"dp\" for Duplicator",
        '\n', "Enter \"cr\" for Caesar crypto")

ent_func = input()
check_ = ent_func.lower()

if check_ == "cl":
    calculator()
elif check_ == "rv":
    reverser()
elif check_ == "dc":
    dictionary()
elif check_ == "dp":
    duplicator()
elif check_ == "cr":
    caesar_crypto()