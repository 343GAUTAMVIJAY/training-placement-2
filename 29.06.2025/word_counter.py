file_path = 'input.txt'  # Replace with your file
with open(file_path, 'r') as file:
    text = file.read()
words = len(text.split())
print(f"Word count: {words}")