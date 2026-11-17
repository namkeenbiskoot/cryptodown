def encrypt(text, key):
    result = ""
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result += chr((ord(c) - base + key) % 26 + base)
        else:
            result += c

    return result

def decrypt(text, key):
    return encrypt(text, -key)

text = input("Enter text ")
key = int(input("Enter key "))

cipher = encrypt(text, key)
print("cipher ", cipher)

pt = decrypt(cipher, key)
print("pt ", pt)