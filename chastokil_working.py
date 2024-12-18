def encrypt_rail_fence(text, key):

    # Створення матриці для "рельсів"
    rail = []
    for i in range(key):
        rail.append(['' for i in range(len(text))])

    # Coords + direction
    dir_down = False
    row = 0
    col = 0

    # муваєм по ячейкам
    for char in text:
        print(char) #test
        if row == 0 or row == key - 1:
            dir_down = not dir_down
            print(row, dir_down, char) #test

        rail[row][col] = char
        col += 1

        # Перехід до наступного рядка
        if dir_down == True:
            row += 1
        else:
            row -= 1

    # Зчитування
    result = []
    for i in range(key):
        for char in rail[i]:
            if char != '':
                result.append(char)

    return ''.join(result)

def decrypt_rail_fence(cipher, key):

    # Створення матриці для "рельсів"
    rail = []
    for i in range(key):
        rail.append(['' for i in range(len(cipher))])

    # Позначення позицій для заповнення
    dir_down = None
    row = 0
    col = 0

    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        # Помітка для заповнення
        rail[row][col] = '*'
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    # Заповнення матриці символами шифротексту
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    # Зчитування символів у зигзагоподібному порядку
    result = []
    row = 0
    col = 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        # Додання символу до результату
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    return ''.join(result)

# TEST
textik= "Пример текста"
key = 3

encrypted = encrypt_rail_fence(textik, key)
decrypted = decrypt_rail_fence(encrypted, key)

print("Original: ", textik)
print("Encrypted: ", encrypted)
print("Decrypted: ", decrypted)
