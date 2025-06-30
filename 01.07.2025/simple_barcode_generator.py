import barcode
from barcode.writer import ImageWriter

code = input("Enter code for barcode: ")
barcode.get('code128', code, writer=ImageWriter()).save('barcode')
print("Barcode saved as barcode.png")