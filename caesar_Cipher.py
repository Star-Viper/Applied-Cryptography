def cc(message, shift):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    alphabets_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''

    for letter in message:
        if letter in alphabets:
            index = (alphabets.index(letter) + shift) % len(alphabets)
            result += alphabets[index]
        elif letter in alphabets_upper:
            index = (alphabets_upper.index(letter) + shift) % len(alphabets_upper)
            result += alphabets_upper[index]
        else:
            result += letter

    return result

def encrypt(message, shift):
    return cc(message, shift)

def decrypt(message, shift):
    return cc(message, -shift)

while True:
    print("\nCaesar Cipher Menu:")
    print("1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Quit")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        original_message = input("Enter the message to encrypt: ")
        shift_value = int(input("Enter the shift value: "))
        encrypted_message = encrypt(original_message, shift_value)
        print(f'Encrypted Message: {encrypted_message}')

    elif choice == '2':
        encrypted_message = input("Enter the message to decrypt: ")
        shift_value = int(input("Enter the shift value: "))
        decrypted_message = decrypt(encrypted_message, shift_value)
        print(f'Decrypted Message: {decrypted_message}')

    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
