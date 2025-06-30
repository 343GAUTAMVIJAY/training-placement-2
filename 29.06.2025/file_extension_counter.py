import os
from collections import Counter

path = 'files'  # Replace with your directory
extensions = [os.path.splitext(file)[1] for root, _, files in os.walk(path) for file in files]
counts = Counter(extensions)
for ext, count in counts.items():
    print(f"{ext or 'No extension'}: {count} files")