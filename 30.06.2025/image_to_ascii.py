from PIL import Image

image_path = 'input.jpg'  # Replace with your image
img = Image.open(image_path).convert('L').resize((80, 40))
ascii_chars = '@%#*+=-:. '
for y in range(img.height):
    for x in range(img.width):
        pixel = img.getpixel((x, y))
        print(ascii_chars[pixel // 32], end='')
    print()