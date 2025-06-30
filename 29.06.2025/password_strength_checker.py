import re

password = input("Enter password: ")
score = 0
if len(password) >= 8:
    score += 1
if re.search(r'[A-Z]', password):
    score += 1
if re.search(r'[0-9]', password):
    score += 1
if re.search(r'[!@#$%^&*]', password):
    score += 1
print("Password strength:", ["Weak", "Moderate", "Strong", "Very Strong"][score-1])