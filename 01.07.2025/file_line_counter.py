file_path = 'input.txt'  # Replace withක

with open(file_path, 'r') as f:
    lines = len(f.readlines())
print(f"Line count: {lines}")