import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("GCD: ", math.gcd(a, b))

num = int(input("Enter Number: "))
mod = int(input("Enter Modulus: "))

try:
    print("Modular inverse: ", pow(num, -1, mod))
except ValueError:
    print("NA")