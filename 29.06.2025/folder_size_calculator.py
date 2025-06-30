import os

path = 'folder'  # Replace with your folder
total_size = sum(os.path.getsize(os.path.join(root, file))
                 for root, _, files in os.walk(path) for file in files)
print(f"Total size: {total_size / 1024:.2f} KB")