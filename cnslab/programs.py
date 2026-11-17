"""
Offline CNS Lab Programs Repository and File Generator.
Contains all lab exam practice programs with zero external network dependencies.
"""

from pathlib import Path
from typing import Dict, Optional, Union

# Exact program code strings
LAB_1_CODE = '''def encrypt(text, key):
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
'''

LAB_2_CODE = '''text = input("Enter pt ").upper()
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
'''

LAB_3_CODE = '''from stegano import lsb

image = input("enter image name: ")
msg = input("enter message: ")

secret = lsb.hide(image, msg)
secret.save("stego.png")
print("Message hidden")

print("Extracted message:", lsb.reveal("stego.png"))
'''

LAB_4_CODE = '''import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("GCD: ", math.gcd(a, b))

num = int(input("Enter Number: "))
mod = int(input("Enter Modulus: "))

try:
    print("Modular inverse: ", pow(num, -1, mod))
except ValueError:
    print("NA")
'''

LAB_5_CODE = '''def modular_exponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def modular_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        return None
    return x % m

print("----- Modular Exponentiation -----")
base = int(input("Enter Base: "))
exponent = int(input("Enter Exponent: "))
modulus = int(input("Enter Modulus: "))
power = modular_exponentiation(base, exponent, modulus)
print("Result =", power)

print("\\n----- Modular Inverse -----")
number = int(input("Enter Number: "))
mod = int(input("Enter Modulus: "))
inverse = modular_inverse(number, mod)
if inverse is None:
    print("Modular Inverse does not exist.")
else:
    print("Modular Inverse =", inverse)
'''

LAB_6_CODE = '''from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key = b'12345678'
text = input("Enter pt: ")

cipher = DES.new(key, DES.MODE_ECB)
enc = cipher.encrypt(pad(text.encode(), 8))
print("Encrypted: ", enc.hex())

dec = cipher.decrypt(enc)
print("decrypted: ", unpad(dec, 8).decode())
'''

LAB_7A_CODE = '''from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'1234567890abcdef'
text = input("Enter pt: ")

cipher = AES.new(key, AES.MODE_ECB)
enc = cipher.encrypt(pad(text.encode(), 16))
print("Encrypted: ", enc.hex())

dec = cipher.decrypt(enc)
print("decrypted: ", unpad(dec, 16).decode())
'''

LAB_7B_CODE = '''from Crypto.Cipher import AES
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
'''

LAB_8_CODE = '''from math import gcd

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
'''

LAB_9_CODE = '''# Diffie-Hellman Key Exchange

p = int(input("Enter Prime Number (p): "))
g = int(input("Enter Primitive Root (g): "))

a = int(input("Enter Alice's Private Key: "))
b = int(input("Enter Bob's Private Key: "))

A = pow(g, a, p)
B = pow(g, b, p)

print("\\nAlice's Public Key:", A)
print("Bob's Public Key  :", B)

Alice_secret = pow(B, a, p)
Bob_secret = pow(A, b, p)

print("\\nAlice's Shared Secret Key:", Alice_secret)
print("Bob's Shared Secret Key  :", Bob_secret)

if Alice_secret == Bob_secret:
    print("\\nSecure Key Exchange Successful!")
else:
    print("\\nKey Exchange Failed!")
'''

LAB_10_CODE = '''import hashlib
import hmac

# Part A: SHA-256 Hash
message = input("Enter Message: ")
hash_value = hashlib.sha256(message.encode()).hexdigest()
print("\\nSHA-256 Hash:")
print(hash_value)

verify = input("\\nEnter Message Again for Verification: ")
verify_hash = hashlib.sha256(verify.encode()).hexdigest()
if hash_value == verify_hash:
    print("\\nHash Verified Successfully.")
else:
    print("\\nHash Verification Failed.")

# Part B: HMAC
key = input("\\nEnter Secret Key: ").encode()
message = input("Enter Message: ").encode()
mac = hmac.new(key, message, hashlib.sha256).hexdigest()
print("\\nGenerated HMAC:")
print(mac)

verify_message = input("\\nEnter Message Again for Verification: ").encode()
verify_mac = hmac.new(key, verify_message, hashlib.sha256).hexdigest()
if mac == verify_mac:
    print("\\nHMAC Verified Successfully.")
else:
    print("\\nHMAC Verification Failed.")
'''

LAB_11_CODE = '''from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate RSA Key Pair
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

message = input("Enter Message: ").encode()

# Hash the message
hash_value = SHA256.new(message)

# Generate Digital Signature
signature = pkcs1_15.new(private_key).sign(hash_value)
print("\\nDigital Signature Generated Successfully.")

# Verification
try:
    pkcs1_15.new(public_key).verify(hash_value, signature)
    print("Digital Signature Verified Successfully.")
except (ValueError, TypeError):
    print("Digital Signature Verification Failed.")
'''

# Catalog of all programs
PROGRAMS: Dict[str, dict] = {
    "1": {
        "filename": "1.py",
        "title": "Caesar Cipher (Encryption & Decryption)",
        "code": LAB_1_CODE,
        "aliases": ["1", "p1", "lab1", "caesar"],
    },
    "2": {
        "filename": "2.py",
        "title": "Transposition Cipher (Encryption & Decryption)",
        "code": LAB_2_CODE,
        "aliases": ["2", "p2", "lab2", "transposition"],
    },
    "3": {
        "filename": "3.py",
        "title": "Image-Based Steganography (LSB)",
        "code": LAB_3_CODE,
        "aliases": ["3", "p3", "lab3", "stego", "steganography"],
    },
    "4": {
        "filename": "4.py",
        "title": "GCD & Modular Inverse (Euclidean)",
        "code": LAB_4_CODE,
        "aliases": ["4", "p4", "lab4", "gcd"],
    },
    "5": {
        "filename": "5.py",
        "title": "Modular Exponentiation & Extended Euclidean Inverse",
        "code": LAB_5_CODE,
        "aliases": ["5", "p5", "lab5", "mod_arith", "modular"],
    },
    "6": {
        "filename": "6.py",
        "title": "DES Encryption & Decryption (ECB Mode)",
        "code": LAB_6_CODE,
        "aliases": ["6", "p6", "lab6", "des"],
    },
    "7a": {
        "filename": "7a.py",
        "title": "AES Encryption & Decryption (ECB Mode)",
        "code": LAB_7A_CODE,
        "aliases": ["7a", "p7a", "lab7a", "aes_ecb"],
    },
    "7b": {
        "filename": "7b.py",
        "title": "AES Encryption & Decryption (CBC Mode)",
        "code": LAB_7B_CODE,
        "aliases": ["7b", "p7b", "lab7b", "aes_cbc"],
    },
    "8": {
        "filename": "8.py",
        "title": "RSA Public Key Cryptosystem",
        "code": LAB_8_CODE,
        "aliases": ["8", "p8", "lab8", "rsa"],
    },
    "9": {
        "filename": "9.py",
        "title": "Diffie-Hellman Key Exchange",
        "code": LAB_9_CODE,
        "aliases": ["9", "p9", "lab9", "diffie_hellman", "dh"],
    },
    "10": {
        "filename": "10.py",
        "title": "Cryptographic Hash (SHA-256) & HMAC",
        "code": LAB_10_CODE,
        "aliases": ["10", "p10", "lab10", "sha", "hmac"],
    },
    "11": {
        "filename": "11.py",
        "title": "Digital Signature Generation & Verification (RSA + SHA-256)",
        "code": LAB_11_CODE,
        "aliases": ["11", "p11", "lab11", "signature", "digital_signature"],
    },
}

# Fast alias lookup
_ALIAS_MAP: Dict[str, str] = {}
for _key, _meta in PROGRAMS.items():
    for _alias in _meta["aliases"]:
        _ALIAS_MAP[_alias.lower()] = _key


def normalize_key(key: Union[int, str]) -> str:
    """Normalize input key (e.g. 1, 'p1', 'lab7a') to standard key ('1', '7a')."""
    k = str(key).strip().lower()
    if k in _ALIAS_MAP:
        return _ALIAS_MAP[k]
    raise KeyError(
        f"Unknown lab program '{key}'. Available programs: {', '.join(PROGRAMS.keys())}"
    )


def get_code(program: Union[int, str]) -> str:
    """Return the code of a specific lab program as a string."""
    key = normalize_key(program)
    return PROGRAMS[key]["code"]


def write_program(
    program: Union[int, str],
    filename: Optional[str] = None,
    dest_dir: Optional[Union[str, Path]] = None,
    overwrite: bool = True,
    quiet: bool = False,
) -> Path:
    """
    Write the code for a lab program to a file.
    
    Args:
        program: Identifier for the lab (e.g. 1, '7a', 'rsa', 'lab3').
        filename: Custom destination filename. Defaults to standard lab filename (e.g. '1.py').
        dest_dir: Target directory (defaults to current working directory).
        overwrite: Overwrite existing file if True (defaults to True).
        quiet: Suppress stdout message if True.
        
    Returns:
        Path: Path object pointing to the created file.
    """
    key = normalize_key(program)
    meta = PROGRAMS[key]
    out_filename = filename or meta["filename"]
    out_path = Path(dest_dir or ".").resolve() / out_filename

    if out_path.exists() and not overwrite:
        if not quiet:
            print(f"[!] Skipped '{out_filename}': file already exists and overwrite=False.")
        return out_path

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(meta["code"], encoding="utf-8")

    if not quiet:
        print(f"[+] Created '{out_filename}' ({meta['title']})")

    return out_path


# Individual functions for each lab program
def lab1(filename: Optional[str] = None, dest_dir: Optional[Union[str, Path]] = None) -> Path:
    """Create Caesar Cipher (1.py)"""
    return write_program("1", filename=filename, dest_dir=dest_dir)

def lab2(filename: Optional[str] = None, dest_dir: Optional[Union[str, Path]] = None) -> Path:
    """Create Transposition Cipher (2.py)"""
    return write_program("2", filename=filename, dest_dir=dest_dir)

def lab3(filename: Optional[str] = None, dest_dir: Optional[Union[str, Path]] = None) -> Path:
    """Create Image-Based Steganography (3.py)"""
    return write_program("3", filename=filename, dest_dir=dest_dir)

def lab4(filename: Optional[str] = None, dest_dir: Optional[Union[str, Path]] = None) -> Path:
    """Create GCD & Modular Inverse (4.py)"""
    return write_program("4", filename=filename, dest_dir=dest_dir)

def lab5(filename: Optional[str] = None, dest_dir: Optional[Union[str, Path]] = None) -> Path:
    """Create Modular Exponentiation & Inverse (5.py)"""
    return write_program("5", filename=filename, dest_dir=dest_dir)

def lab6(filename: Optional[str] = None, dest_dir: Optional[Union[str, Path]] = None) -> Path:
    """Create DES Cipher (6.py)"""
    return write_program("6", filename=filename, dest_dir=dest_dir)

def lab7a(filename: Optional[str] = None, dest_dir: Optional[Union[str, Path]] = None) -> Path:
    """Create AES ECB Mode (7a.py)"""
    return write_program("7a", filename=filename, dest_dir=dest_dir)

def lab7b(filename: Optional[str] = None, dest_dir: Optional[Union[str, Path]] = None) -> Path:
    """Create AES CBC Mode (7b.py)"""
    return write_program("7b", filename=filename, dest_dir=dest_dir)

def lab8(filename: Optional[str] = None, dest_dir: Optional[Union[str, Path]] = None) -> Path:
    """Create RSA Cryptosystem (8.py)"""
    return write_program("8", filename=filename, dest_dir=dest_dir)

def lab9(filename: Optional[str] = None, dest_dir: Optional[Union[str, Path]] = None) -> Path:
    """Create Diffie-Hellman Key Exchange (9.py)"""
    return write_program("9", filename=filename, dest_dir=dest_dir)

def lab10(filename: Optional[str] = None, dest_dir: Optional[Union[str, Path]] = None) -> Path:
    """Create SHA-256 & HMAC (10.py)"""
    return write_program("10", filename=filename, dest_dir=dest_dir)

def lab11(filename: Optional[str] = None, dest_dir: Optional[Union[str, Path]] = None) -> Path:
    """Create Digital Signature RSA + SHA-256 (11.py)"""
    return write_program("11", filename=filename, dest_dir=dest_dir)


# Short aliases p1..p11
p1 = lab1
p2 = lab2
p3 = lab3
p4 = lab4
p5 = lab5
p6 = lab6
p7a = lab7a
p7b = lab7b
p8 = lab8
p9 = lab9
p10 = lab10
p11 = lab11

# Descriptive aliases
caesar = lab1
transposition = lab2
stego = lab3
steganography = lab3
gcd = lab4
mod_arith = lab5
des = lab6
aes_ecb = lab7a
aes_cbc = lab7b
rsa = lab8
diffie_hellman = lab9
sha = lab10
hmac = lab10
digital_signature = lab11


def create_all(dest_dir: Optional[Union[str, Path]] = None, overwrite: bool = True) -> Dict[str, Path]:
    """
    Generate all lab program files at once in the specified directory.
    
    Args:
        dest_dir: Target directory (default: current directory).
        overwrite: Overwrite existing files (default: True).
        
    Returns:
        dict: Mapping of program key to created Path object.
    """
    created = {}
    print("=" * 60)
    print("Creating all CNS Lab practice programs (Offline)...")
    print("=" * 60)
    for key in PROGRAMS:
        created[key] = write_program(key, dest_dir=dest_dir, overwrite=overwrite)
    print("=" * 60)
    print(f"Successfully generated {len(created)} lab programs.")
    return created


dump_all = create_all


def list_programs() -> None:
    """Print a clean table of all available lab programs and their functions."""
    print("=" * 75)
    print(f"{'Key':<6} {'Filename':<10} {'Function':<12} {'Description'}")
    print("-" * 75)
    for key, meta in PROGRAMS.items():
        fn_name = f"p{key}()"
        print(f"{key:<6} {meta['filename']:<10} {fn_name:<12} {meta['title']}")
    print("=" * 75)
    print("Usage:")
    print("  import cnslab")
    print("  cnslab.p1()       # Creates 1.py")
    print("  cnslab.p7a()      # Creates 7a.py")
    print("  cnslab.create_all() # Creates all files")
    print("=" * 75)


def create_sample_image(filename: str = "image.png", dest_dir: Optional[Union[str, Path]] = None) -> Path:
    """
    Creates a minimal valid PNG image completely offline for testing Lab 3 (Steganography).
    Uses a hardcoded base64/binary PNG header without needing PIL or external tools.
    """
    # 1x1 valid RGB PNG bytes
    png_bytes = (
        b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02'
        b'\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDATx\x9cc\xf8\xcf\xc0\x00\x00\x03\x01'
        b'\x01\x00\x18\xdd\x8d\xb0\x00\x00\x00\x00IEND\xaeB`\x82'
    )
    out_path = Path(dest_dir or ".").resolve() / filename
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(png_bytes)
    print(f"[+] Created sample offline image '{filename}' for Steganography.")
    return out_path
