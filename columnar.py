def encrypt(pt, col):
    if len(pt) % col == 0:
        rows = len(pt) // col
    else:
        rows = len(pt) // col + 1

    matrix = [['' for _ in range(col)] for _ in range(rows)]

    char_index = 0
    for row in range(rows):
        for key in range(col):
            if char_index < len(pt):
                matrix[row][key] = pt[char_index]
                char_index += 1
            else:
                break

    transposed_matrix = [['' for _ in range(rows)] for _ in range(col)]
    for i in range(rows):
        for j in range(col):
            transposed_matrix[j][i] = matrix[i][j]

    encrypted_string = ''.join(''.join(row) for row in transposed_matrix)
    
    return encrypted_string

def decrypt(encrypted_str, col):
    rows = len(encrypted_str) // col
    if len(encrypted_str) % col != 0:
        rows += 1

    matrix = [['' for _ in range(col)] for _ in range(rows)]

    char_index = 0
    for row_index in range(rows):
        for col_index in range(col):
            if char_index < len(encrypted_str):
                matrix[row_index][col_index] = encrypted_str[char_index]
                char_index += 1

    original_str = ''
    for col_index in range(col):
        for row_index in range(rows):
            original_str += matrix[row_index][col_index]

    original_str = original_str[:len(encrypted_str)]

    return original_str

encrypted_result = encrypt('maam', 3)
print("Encrypted:", encrypted_result)

decrypted_result = decrypt(encrypted_result, 3)
print("Decrypted:", decrypted_result)
