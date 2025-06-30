file_path = 'input.txt'  # Replace with your file
with open(file_path, 'r') as f:
    lines = f.readlines()
unique_lines = list(dict.fromkeys(lines))
with open(file_path, 'w') as f:
    f.writelines(unique_lines)
print("Duplicates removed.")