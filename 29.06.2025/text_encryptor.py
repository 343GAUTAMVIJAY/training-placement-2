def encrypt(text, shift):
    return ''.join(chr((ord(c) + shift - 65) % 26 + 65) if c.isalpha() else c for c in text.upper())

text = input("Enter text to encrypt: ")
shift = int(input("Enter shift value: "))
print("Encrypted:", encrypt(text, shift))