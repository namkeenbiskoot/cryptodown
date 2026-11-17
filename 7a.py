from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'1234567890abcdef'
text = input("Enter pt: ")

cipher = AES.new(key, AES.MODE_ECB)
enc = cipher.encrypt(pad(text.encode(), 16))
print("Encrypted: ", enc.hex())

dec = cipher.decrypt(enc)
print("decrypted: ", unpad(dec, 16).decode())