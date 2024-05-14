def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_superincreasing_sequence(n):
    sequence = [1]
    for i in range(n - 1):
        sequence.append(sum(sequence) + 1)
    return sequence

def generate_public_key(superincreasing_seq, multiplier, modulus):
    return [(multiplier * x) % modulus for x in superincreasing_seq]

def encrypt(message, public_key):
    return sum(message[i] * public_key[i] for i in range(len(message)))

def decrypt(encrypted, superincreasing_seq, multiplier, modulus):
    decrypted = []
    inverse_multiplier = mod_inverse(multiplier, modulus)
    t = (encrypted * inverse_multiplier) % modulus

    for i in reversed(superincreasing_seq):
        if t >= i:
            decrypted.append(1)
            t -= i
        else:
            decrypted.append(0)
    return list(reversed(decrypted))

n = int(input("Enter the number of elements in the superincreasing sequence: "))
superincreasing_seq = generate_superincreasing_sequence(n)
print("Superincreasing sequence:", superincreasing_seq)
multiplier = int(input("Enter the multiplier: "))
modulus = int(input("Enter the modulus: "))
public_key = generate_public_key(superincreasing_seq, multiplier, modulus)
print("Public key:", public_key)

message = list(map(int, input("Enter the message (0s and 1s separated by spaces): ").split()))
if len(message) != n:
    print("Invalid message length. It should have the same length as the superincreasing sequence.")

encrypted = encrypt(message, public_key)
print("Encrypted message:", encrypted)

decrypted = decrypt(encrypted, superincreasing_seq, multiplier, modulus)
print("Decrypted message:", decrypted)

