text = input("Enter text: ")
binary = ' '.join(format(ord(c), '08b') for c in text)
print("Binary:", binary)