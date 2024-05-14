import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9000 
# Connect to server
client_socket.connect((host, port))

plaintext = input("Enter plaintext: ")

# Send plaintext to server
client_socket.send(plaintext.encode())

choice = input("Do you want to encrypt or decrypt? ")

# Send choice to server
client_socket.send(choice.encode())

key = int(input("Enter key: "))
client_socket.send(str(key).encode())

# Receive response from server
response = client_socket.recv(1024).decode()

print("Response from server:", response)

# Close the connection
client_socket.close()