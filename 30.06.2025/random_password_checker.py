import random
import string
import re

password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(12))
score = sum([len(password) >= 8, bool(re.search(r'[A-Z]', password)), bool(re.search(r'[0-9]', password)), bool(re.search(r'[!@#$%^&*]', password))])
print(f"Password: {password}")
print("Strength:", ["Weak", "Moderate", "Strong", "Very Strong"][score-1])