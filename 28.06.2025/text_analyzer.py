from collections import Counter
import re

text = input("Enter text: ")
words = re.findall(r'\b\w+\b', text.lower())
sentences = len(re.split(r'[.!?]+', text)) - 1
common_word = Counter(words).most_common(1)
print(f"Word count: {len(words)}")
print(f"Sentence count: {sentences}")
print(f"Most common word: {common_word[0][0]} ({common_word[0][1]} times)")