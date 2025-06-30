import os
import time

file_path = input("Enter file path: ")
stats = os.stat(file_path)
print(f"Size: {stats.st_size} bytes")
print(f"Created: {time.ctime(stats.st_ctime)}")