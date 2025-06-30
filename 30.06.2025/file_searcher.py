import os

path = 'files'  # Replace with your directory
keyword = input("Enter keyword: ")
for root, _, files in os.walk(path):
    for file in files:
        if keyword.lower() in file.lower():
            print(os.path.join(root, file))