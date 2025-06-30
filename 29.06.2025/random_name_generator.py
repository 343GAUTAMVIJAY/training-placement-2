import random

first_names = ['Alice', 'Bob', 'Charlie', 'Diana']
last_names = ['Smith', 'Johnson', 'Brown', 'Davis']
for _ in range(5):
    print(f"{random.choice(first_names)} {random.choice(last_names)}")