import json

input_path = r'C:\Users\kidus\OneDrive\Documents\GitHub\nosql-challenge\Starter_Code\Resources\establishments.json'
output_path = r'C:\Users\kidus\OneDrive\Documents\GitHub\nosql-challenge\Starter_Code\Resources\establishments.jsonl'

# Load the JSON array from the input file with utf-8 encoding
with open(input_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Write out each object in the array as a separate line in the output file
with open(output_path, 'w', encoding='utf-8') as file:
    for entry in data:
        json.dump(entry, file)
        file.write('\n')
