from math import gcd

p,q = 17, 11
n = p * q
phi = (p - 1) * (q - 1)
e = 7
d = pow(e, -1, phi)

print("Public key: ", (e, n))
print("Private key: ", (d, n))

text = input("Enter pt: ")

cipher = [pow(ord(c), e, n) for c in text]
print("Encrypted: ", cipher)

plain = ''. join(chr(pow(c, d, n)) for c in cipher)
print("pt:", plain)
