def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def encrypt(text, key1, key2):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr(((key1 * (ord(char) - 65) + key2) % 26) + 65)
            else:
                result += chr(((key1 * (ord(char) - 97) + key2) % 26) + 97)
        else:
            result += char
    print(result) 

def decrypt(text, key1, key2):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr(((mod_inverse(key1, 26) * (ord(char) - 65 - key2)) % 26) + 65)
            else:
                result += chr(((mod_inverse(key1, 26) * (ord(char) - 97 - key2)) % 26) + 97)
        else:
            result += char
    print(result)

while True:
    print("Affine Cipher Menu:")
    print("1. Encryption")
    print("2. Decryption")
    print("3. Exit")

    choice = input("Enter your choice: ")
    
    if choice == '1':
        plain_text = input("Enter the plain text: ")
        key1 = int(input("Enter key 1: "))
        key2 = int(input("Enter key 2: "))
        encrypt(plain_text, key1, key2)
    elif choice == '2':
        cipher_text = input("Enter the cipher text: ")
        key1 = int(input("Enter key 1: "))
        key2 = int(input("Enter key 2: "))
        decrypt(cipher_text, key1, key2)
    elif choice == '3':
        break
    else:
        print("Enter valid choice")