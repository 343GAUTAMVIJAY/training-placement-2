import os

path = 'files'  # Replace with your directory
prefix = input("Enter prefix for files: ")
for i, file in enumerate(os.listdir(path), 1):
    if os.path.isfile(os.path.join(path, file)):
        ext = os.path.splitext(file)[1]
        os.rename(os.path.join(path, file), os.path.join(path, f"{prefix}_{i}{ext}"))
print("Files renamed.")