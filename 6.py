from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key = b'12345678'
text = input("Enter pt: ")

cipher = DES.new(key, DES.MODE_ECB)
enc = cipher.encrypt(pad(text.encode(), 8))
print("Encrypted: ", enc.hex())

dec = cipher.decrypt(enc)
print("decrypted: ", unpad(dec, 8).decode())