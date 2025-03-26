import math

# USCLN
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Ham tao khoa RSA
def generate_rsa_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Tim e (la so nguyen to cung nhau)
    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1

    # Tìm d (khoa giai ma d sao cho e*d ≡ 1 (mod phi))
    d = pow(e, -1, phi)
    return (e, n), (d, n)  # tra ve khoa cong khai va khoa bi mat

# Ham ma hoa RSA
def rsa_encrypt(plaintext, public_key):
    e, n = public_key
    # Chuyen van ban thanh so nguyen roi ma hoa tung ky tu
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

# Ham giai ma RSA
def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    # Giai ma roi chuyen tung so nguyen thanh ky tu
    decrypted = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return decrypted

p = int(input("Nhập số nguyên tố p: "))  # Số nguyên tố
q = int(input("Nhập số nguyên tố q: "))  # Số nguyên tố

public_key, private_key = generate_rsa_keys(p, q)
print("Khóa công khai:", public_key)
print("Khóa riêng:", private_key)
plaintext = input("Nhập đoạn văn bản cần mã hóa: ")
encrypted = rsa_encrypt(plaintext, public_key)
print("Dữ liệu đã mã hóa:", encrypted)
decrypted = rsa_decrypt(encrypted, private_key)
print("Dữ liệu đã giải mã:", decrypted)
