text = input("Enter pt ").upper()
key = int(input("Enter key "))

while len(text) % key != 0:
    text += 'X'

cipher = ""

for i in range(key):
    for j in range(i, len(text), key):
        cipher += text[j]

print("cipher ", cipher)

rows = len(cipher) // key
plain = ""

for i in range(rows):
    for j in range(key):
        plain += cipher[j * rows + 1]
print("Decrypt:", plain.rstrip('X'))