import os
import time

path = 'files'  # Replace with your directory
known = set(os.listdir(path))
while True:
    current = set(os.listdir(path))
    new_files = current - known
    if new_files:
        print(f"New files: {new_files}")
        known = current
    time.sleep(5)