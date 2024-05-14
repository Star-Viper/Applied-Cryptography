def is_primitive_root(g, p):
    if pow(g, 1, p) == 1:
        return False
    totient = p - 1
    factors = [2]
    for possible_factor in range(3, totient, 2):
        if possible_factor * possible_factor > totient:
            break
        if totient % possible_factor == 0:
            factors.append(possible_factor)
            factors.append(totient // possible_factor)
    return all(pow(g, totient // factor, p) != 1 for factor in factors)

def find_primitive_root(p):
    for g in range(2, p):
        if is_primitive_root(g, p):
            return g
    return None

def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return result

def diffie_hellman(p, g):
    a = int(input("Enter private key for sender: "))
    b = int(input("Enter private key for receiver: "))
    
    A = mod_exp(g, a, p)
    B = mod_exp(g, b, p)
    
    K1 = mod_exp(B, a, p)
    K2 = mod_exp(A, b, p)
    
    shared_key_equal = K1 == K2
    
    return K1, K2, shared_key_equal

if __name__ == "__main__":
    p = int(input("Enter the shared prime number (p): "))
    
    g = find_primitive_root(p)
    if g is None:
        print("No primitive root found for the given prime number.")
        exit()
    
    print("Primitive root:", g)
    
    shared_key_sender, shared_key_receiver, shared_key_equal = diffie_hellman(p, g)
    
    print("Shared secret key for sender:", shared_key_sender)
    print("Shared secret key for receiver:", shared_key_receiver)
    
    if shared_key_equal:
        print("Both shared secret keys are equal.")
    else:
        print("Shared secret keys are not equal.")
