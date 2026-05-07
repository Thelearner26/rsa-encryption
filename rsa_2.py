def gcd(a , b):
    if b == 0:
        return a 
    return gcd(b , a % b)

# returns the value of phi(n)'s multiple k , the value of the gcd between e and phi(n) , and value of d
def extended_gcd(a , b):
    if a == 0:
        return b , 0 , 1
    result , x1 , y1 = extended_gcd(b % a , a)
    x = y1 - (b // a) * x1
    y = x1      
    return result , x , y


# checks and returns the value of d
def mod_inverse(e , phi):
    result , x , _ = extended_gcd(e , phi)
    if result != 1:
        raise Exception("No modular inverse exists")
    return x % phi


# returns the values of e , d and n
def generate_keys(p , q):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 65537
    if gcd(e, phi_n) != 1:
        e = 2
        while gcd(e, phi_n) != 1:
            e += 1
    d = mod_inverse(e , phi_n)
    return e , d , n


def encrypt_text(message , e , n):
    return [pow(ord(char) , e , n) for char in message]


def decrypt_text(ciphertext , d , n):
    return ''.join([chr(pow(num , d , n)) for num in ciphertext])


# prime numbers 
p = 61
q = 53

e , d , n = generate_keys(p , q)

print (f"The value of n = {n} \n The value of e = {e} \n The value of d = {d}.")


message = input("\nEnter message to encrypt. ")

print(f"Original message: {message}")

ciphertext = encrypt_text(message , e , n)
print(f"Encrypted: {ciphertext}")

decrypted = decrypt_text(ciphertext , d , n)
print(f"Decrypted: {decrypted}")

print(f"\nSuccessful recovery = {message == decrypted}")

























