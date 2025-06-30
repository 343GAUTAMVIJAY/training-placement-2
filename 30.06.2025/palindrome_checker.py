word = input("Enter word: ").lower()
print(f"{word} is {'a palindrome' if word == word[::-1] else 'not a palindrome'}")