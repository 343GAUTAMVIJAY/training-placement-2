import zipfile

file_path = input("Enter file to compress: ")
with zipfile.ZipFile('output.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    z.write(file_path)
print("File compressed as output.zip")