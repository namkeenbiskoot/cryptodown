from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

key = b'1234567890abcdef'
iv = get_random_bytes(16)
text = input("Enter pt: ")

cipher = AES.new(key, AES.MODE_CBC, iv)
enc = cipher.encrypt(pad(text.encode(), 16))
print("Encrypted: ", enc.hex())

cipher = AES.new(key, AES.MODE_CBC, iv)
dec = cipher.decrypt(enc)
print("decrypted: ", unpad(dec, 16).decode())