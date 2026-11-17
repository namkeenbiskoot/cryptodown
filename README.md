# cryptodown (Offline CNS Lab Program Generator)

An offline Python package that generates all Cryptography and Network Security (CNS) laboratory exam programs with a single function call or CLI command.

Works **100% offline** with zero external network requests and zero non-standard runtime dependencies for the generator.

---

## 🚀 Quick Start & Installation

### Option 1: Install from GitHub
```bash
pip install git+https://github.com/namkeenbiskoot/cryptodown.git
```

### Option 2: Install from source folder (Offline)
In this directory, open a terminal and run:
```bash
pip install .
```

### Option 3: Install from pre-built Wheel (`.whl`)
You can copy the built `.whl` from the `dist/` directory to any lab computer (even one without internet) and run:
```bash
pip install cryptodown-1.0.0-py3-none-any.whl
```

---

## 🐍 Python Usage

You can import `cryptodown` (or `cnslab`) in any Python shell or script and call the function for the lab program you need:

```python
import cryptodown as cns

# Generates 1.py (Caesar Cipher)
cns.p1()

# Generates 7a.py (AES ECB)
cns.p7a()

# Generates 8.py (RSA)
cns.p8()

# Generate ALL lab files at once (1.py - 11.py)
cns.create_all()

# View catalog of all programs
cns.list_programs()
```

### Alternatively, use star import:
```python
from cryptodown import *

p1()    # creates 1.py
p2()    # creates 2.py
p6()    # creates 6.py
p7b()   # creates 7b.py
```

### Custom Filenames & Output Directories
Every function accepts an optional `filename` and `dest_dir`:
```python
cns.p1(filename="my_caesar.py")
cns.p8(dest_dir="./output_folder")
```

---

## 💻 Terminal / CLI Usage

Once installed, use `cryptodown`, `cnslab`, or `cns` directly from your command prompt:

```bash
# Generate 1.py
cryptodown 1

# Generate 7a.py
cryptodown 7a

# Generate all lab programs
cryptodown all

# List all available programs
cryptodown list

# Print code to terminal without creating a file
cryptodown 1 --print

# Generate sample 1x1 image for steganography testing
cryptodown image
```

*(You can also invoke via python module: `python -m cryptodown 1`)*

---

## 📋 Available Lab Programs & Functions

| Lab | Function(s) | Default File | Algorithm / Topic |
|---|---|---|---|
| **1** | `p1()`, `lab1()`, `caesar()` | `1.py` | Caesar Cipher (Encrypt & Decrypt) |
| **2** | `p2()`, `lab2()`, `transposition()` | `2.py` | Transposition Cipher (Columnar) |
| **3** | `p3()`, `lab3()`, `stego()` | `3.py` | Image-Based Steganography (LSB) |
| **4** | `p4()`, `lab4()`, `gcd()` | `4.py` | GCD & Modular Inverse (Euclidean) |
| **5** | `p5()`, `lab5()`, `mod_arith()` | `5.py` | Modular Exponentiation & Extended GCD |
| **6** | `p6()`, `lab6()`, `des()` | `6.py` | DES Encryption & Decryption (ECB) |
| **7a**| `p7a()`, `lab7a()`, `aes_ecb()` | `7a.py` | AES Encryption & Decryption (ECB Mode) |
| **7b**| `p7b()`, `lab7b()`, `aes_cbc()` | `7b.py` | AES Encryption & Decryption (CBC Mode) |
| **8** | `p8()`, `lab8()`, `rsa()` | `8.py` | RSA Public Key Cryptosystem |
| **9** | `p9()`, `lab9()`, `diffie_hellman()` | `9.py` | Diffie-Hellman Key Exchange |
| **10**| `p10()`, `lab10()`, `sha()`, `hmac()` | `10.py` | SHA-256 Hash & HMAC Verification |
| **11**| `p11()`, `lab11()`, `digital_signature()` | `11.py` | Digital Signature (RSA + SHA-256) |

---

## 📦 Running the Generated Programs

The generator itself requires only the standard library. The generated lab programs use standard security libraries commonly pre-installed or required for the lab:
- `pycryptodome` (for DES, AES, RSA signatures): `pip install pycryptodome`
- `stegano` (for Lab 3 steganography): `pip install stegano`
- `math`, `hashlib`, `hmac` are built into Python.
