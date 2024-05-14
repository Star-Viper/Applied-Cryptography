import socket

def encrypt(plaintext, key):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            shifted = ord(char) + key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(ciphertext, key):
    return encrypt(ciphertext, -key)

# Creation a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9000 

# Bind to the port
server_socket.bind((host, port))
server_socket.listen(1)

print("Server listening on {}:{}".format(host, port))

while True:
    client_socket, addr = server_socket.accept()
    print("Got a connection from {}".format(addr))
    plaintext = client_socket.recv(1024).decode()
    print("Received plaintext:", plaintext)
    choice = client_socket.recv(1024).decode()
    
    if choice == 'encrypt':
        key = int(client_socket.recv(1024).decode())

        ciphertext = encrypt(plaintext, key)
        print("Encrypted text:", ciphertext)

        client_socket.send(ciphertext.encode())
    elif choice == 'decrypt':
        key = int(client_socket.recv(1024).decode())
        
        decrypted_text = decrypt(plaintext, key)
        print("Decrypted text:", decrypted_text)

        client_socket.send(decrypted_text.encode())
    
    # Close the connection
    client_socket.close()