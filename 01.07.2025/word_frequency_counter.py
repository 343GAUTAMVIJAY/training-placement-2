from collections import Counter

file_path = 'input.txt'  # Replace with your file
with open(file_path, 'r') as f:
    words = f.read().lower().split()
freq = Counter(words).most_common(5)
for word, count in freq:
    print(f"{word}: {count}")