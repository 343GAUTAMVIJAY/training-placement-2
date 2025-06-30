file_path = 'input.txt'  # Replace with your file
old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")
with open(file_path, 'r') as f:
    text = f.read()
text = text.replace(old_word, new_word)
with open(file_path, 'w') as f:
    f.write(text)
print("Text replaced.")