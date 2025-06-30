import json

input_file = 'data.json'  # Replace with your JSON file
output_file = 'formatted.json'
with open(input_file, 'r') as f:
    data = json.load(f)
with open(output_file, 'w') as f:
    json.dump(data, f, indent=4)
print(f"Formatted JSON saved as {output_file}")