import csv
import json

input_file = 'data.csv'  # Replace with your CSV file
output_file = 'data.json'
data = []
with open(input_file, 'r') as f:
    reader = csv.DictReader(f)
    data = [row for row in reader]
with open(output_file, 'w') as f:
    json.dump(data, f, indent=4)
print(f"CSV converted to {output_file}")