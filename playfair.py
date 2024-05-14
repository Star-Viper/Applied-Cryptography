def prepare_input(text):
    return text.lower().replace(" ", "")

def generate_key_table(key):
    key = key.lower().replace(" ", "").replace("j", "i")
    key_matrix = []
    alphabet = "abcdefghiklmnopqrstuvwxyz"

    for char in key + alphabet:
        if char not in key_matrix:
            key_matrix.append(char)

    key_matrix = [key_matrix[i:i+5] for i in range(0, 25, 5)]
    return key_matrix

def find_coordinates(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def encrypt_pair(matrix, pair):
    char1, char2 = pair
    row1, col1 = find_coordinates(matrix, char1)
    row2, col2 = find_coordinates(matrix, char2)

    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5], matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1], matrix[(row2 + 1) % 5][col2]
    else:
        return matrix[row1][col2], matrix[row2][col1]

def encrypt(plaintext, key):
    plaintext = prepare_input(plaintext)
    
    key_matrix = generate_key_table(key)
    
    i =  0
    while i < len(plaintext) -  1:
        if plaintext[i] == plaintext[i +  1]:
            plaintext = plaintext[:i+1] + 'x' + plaintext[i+1:]
        else:
            i +=  1
    
    pairs = [plaintext[i:i+2] for i in range(0, len(plaintext),  2)]
    
    if len(pairs[-1]) ==  1:
        pairs[-1] += 'x'
    
    ciphertext = ""
    for pair in pairs:
        encrypted_pair = encrypt_pair(key_matrix, pair)
        ciphertext += ''.join(encrypted_pair)
    
    return ciphertext

while True:
    print("\nMenu:")
    print("1. Encrypt text")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        plaintext = input("Enter the plaintext: ")
        key = input("Enter the key: ")
        print("Cipher:", encrypt(plaintext, key))
    elif choice == '2':
        break
    else:
        print("Invalid choice. Please try again.")
