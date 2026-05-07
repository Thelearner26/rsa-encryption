def gcd(a , b):
    if b == 0:
        return a
    return gcd(b , a % b)


def extended_gcd(a , b):
    if a == 0:
        return b , 0, 1
    gcd, x1, y1 = extended_gcd(b % a , a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd , x , y


def mod_inverse(e , phi):
    result , x, _ = extended_gcd(e , phi)
    if result != 1:
        raise Exception("No modular inverse exists")
    return x % phi


def generate_keys(p , q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e — coprime to phi, commonly 65537
    e = 65537
    if gcd(e , phi) != 1:
        # Find valid e if 65537 doesn't work
        e = 2
        while gcd(e , phi) != 1:
            e += 1

    # Find d — modular inverse of e
    d = mod_inverse(e , phi)

    return (e , n), (d , n)  # public key, private key


def encrypt(message , e , n):
    return pow(message , e , n)


def decrypt(ciphertext , d , n):
    return pow(ciphertext , d , n)


# Test it
p = 61
q = 53

public_key, private_key = generate_keys(p , q)
e , n = public_key
d , _ = private_key

print(f"Public key: (e={e} , n={n})")
print(f"Private key: (d={d} , n={n})")
print(f"phi(n) = {(p-1)*(q-1)}")

message = 42
print(f"\nOriginal message: {message}")

ciphertext = encrypt(message , e , n)
print(f"Encrypted: {ciphertext}")

decrypted = decrypt(ciphertext , d , n)
print(f"Decrypted: {decrypted}")

print(f"\nSuccessfully recovered: {message == decrypted}")