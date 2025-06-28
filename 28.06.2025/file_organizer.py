# Organizes files in a directory by extension
import os
import shutil

def organize_files(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(filename):
            ext = os.path.splitext(filename)[1][1:]
            if ext:
                os.makedirs(ext, exist_ok=True)
                shutil.move(filename, os.path.join(ext, filename))
    print("Files organized!")

if __name__ == "__main__":
    organize_files(".")