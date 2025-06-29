import json

input_file = 'db_cleaned_nobom.json'
output_file = 'db_cleaned_nobom_stripped.json'

with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Filter out contenttypes
filtered = [obj for obj in data if obj.get('model') != 'contenttypes.contenttype']

print(f"Removed {len(data) - len(filtered)} contenttypes entries.")

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(filtered, f, indent=2)

print(f"Cleaned fixture saved to: {output_file}")
