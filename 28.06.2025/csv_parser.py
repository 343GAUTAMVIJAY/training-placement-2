import csv

file_path = 'data.csv'  # Replace with your CSV file
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)
    print("|".join(headers))
    print("-" * len("|".join(headers)))
    for row in reader:
        print("|".join(row))