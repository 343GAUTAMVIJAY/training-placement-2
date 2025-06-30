word1 = input("Enter first word: ").lower()
word2 = input("Enter second word: ").lower()
print(f"Anagrams: {sorted(word1) == sorted(word2)}")