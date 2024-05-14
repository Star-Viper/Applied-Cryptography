import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def euler_totient(p, q):
    return (p - 1) * (q - 1)

def find_e(phi):
    e = 2
    while True:
        if gcd(e, phi) == 1:
            return e
        e += 1

def find_d(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None

def encrypt(msg, e, n):
    return pow(msg, e, n)

def decrypt(msg, d, n):
    return pow(msg, d, n)

p = int(input("Enter a prime number p: "))
q = int(input("Enter a prime number q: "))
        
n = p * q
print("n =", n)
        
phi = euler_totient(p, q)
e = find_e(phi)
print("Private key exponent d =", e)
        
d = find_d(e, phi)
print("Public key exponent e =", d)
        
print("Private Key: (d, n) = ({}, {})".format(e, n))
print("Public Key: (e, n) = ({}, {})".format(d, n))
        
msg = int(input("\nEnter a message to encrypt: "))
encrypted_msg = encrypt(msg, e, n)
print("Encrypted message =", encrypted_msg)
        
decrypted_msg = decrypt(encrypted_msg, d, n)
print("Decrypted message =", decrypted_msg)


