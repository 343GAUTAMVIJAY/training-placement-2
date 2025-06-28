# Resizes an image using Pillow
from PIL import Image

def resize_image(input_path, output_path, size=(100, 100)):
    img = Image.open(input_path)
    img_resized = img.resize(size)
    img_resized.save(output_path)
    print(f"Image saved to {output_path}")

if __name__ == "__main__":
    resize_image("input.jpg", "output.jpg", size=(200, 200))