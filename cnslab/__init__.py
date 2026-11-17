"""
CNSLab - Offline Python package to generate all CNS Lab Exam practice programs.

Functions:
    p1(), lab1(), caesar()             -> Generates '1.py'
    p2(), lab2(), transposition()      -> Generates '2.py'
    p3(), lab3(), stego()              -> Generates '3.py'
    p4(), lab4(), gcd()                -> Generates '4.py'
    p5(), lab5(), mod_arith()          -> Generates '5.py'
    p6(), lab6(), des()                -> Generates '6.py'
    p7a(), lab7a(), aes_ecb()          -> Generates '7a.py'
    p7b(), lab7b(), aes_cbc()          -> Generates '7b.py'
    p8(), lab8(), rsa()                -> Generates '8.py'
    p9(), lab9(), diffie_hellman()     -> Generates '9.py'
    p10(), lab10(), sha(), hmac()      -> Generates '10.py'
    p11(), lab11(), digital_signature()-> Generates '11.py'

Bulk & Utility:
    create_all() / dump_all() / all()  -> Generates all lab programs at once
    list_programs()                    -> Displays catalog of all lab programs
    get_code(program)                  -> Returns code as a string
    create_sample_image()              -> Generates minimal valid 'image.png'
"""

from .programs import (
    # Lab numbered functions
    lab1, lab2, lab3, lab4, lab5, lab6, lab7a, lab7b, lab8, lab9, lab10, lab11,
    p1, p2, p3, p4, p5, p6, p7a, p7b, p8, p9, p10, p11,
    # Semantic aliases
    caesar, transposition, stego, steganography, gcd, mod_arith,
    des, aes_ecb, aes_cbc, rsa, diffie_hellman, sha, hmac, digital_signature,
    # Utilities
    create_all, dump_all, list_programs, get_code, write_program, create_sample_image,
    PROGRAMS,
)

# Friendly 'all' alias
all = create_all

__version__ = "1.0.0"

__all__ = [
    "lab1", "lab2", "lab3", "lab4", "lab5", "lab6", "lab7a", "lab7b", "lab8", "lab9", "lab10", "lab11",
    "p1", "p2", "p3", "p4", "p5", "p6", "p7a", "p7b", "p8", "p9", "p10", "p11",
    "caesar", "transposition", "stego", "steganography", "gcd", "mod_arith",
    "des", "aes_ecb", "aes_cbc", "rsa", "diffie_hellman", "sha", "hmac", "digital_signature",
    "create_all", "dump_all", "all", "list_programs", "get_code", "write_program",
    "create_sample_image", "PROGRAMS", "__version__"
]
