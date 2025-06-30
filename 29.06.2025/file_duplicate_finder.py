import os
from collections import defaultdict

path = 'files'  # Replace with your directory
sizes = defaultdict(list)
for root, _, files in os.walk(path):
    for file in files:
        file_path = os.path.join(root, file)
        sizes[os.path.getsize(file_path)].append(file_path)
for size, paths in sizes.items():
    if len(paths) > 1:
        print(f"Duplicates (size {size} bytes): {paths}")