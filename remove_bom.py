# remove_bom.py

input_file = "db_cleaned_utf8.json"
output_file = "db_cleaned_nobom.json"

with open(input_file, "r", encoding="utf-8-sig") as f:
    data = f.read()

with open(output_file, "w", encoding="utf-8") as f:
    f.write(data)

print("✅ BOM removed and saved to", output_file)
