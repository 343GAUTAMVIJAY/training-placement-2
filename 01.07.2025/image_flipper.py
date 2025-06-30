from PIL import Image

image_path = 'input.jpg'  # Replace with your image
output_path = 'flipped.jpg'
img = Image.open(image_path)
img = img.transpose(Image.FLIP_LEFT_RIGHT)
img.save(output_path)
print(f"Flipped image saved as {output_path}")