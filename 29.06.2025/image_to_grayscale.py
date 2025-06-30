from PIL import Image

image_path = 'input.jpg'  # Replace with your image
output_path = 'grayscale.jpg'
img = Image.open(image_path).convert('L')
img.save(output_path)
print(f"Grayscale image saved as {output_path}")