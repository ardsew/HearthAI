import json


# Load the JSON file
file_path = 'hearthstone_standard_cards_11_29_2024.json'

with open(file_path, 'r') as file:
    data = json.load(file)

# Keys to remove
keys_to_remove = ['artist', 'collectible', 'dbfId', 'flavor']

# Remove the keys from each entry
for entry in data:
    for key in keys_to_remove:
        entry.pop(key, None)  # Use pop with default to avoid errors if the key is missing

# Save the modified JSON back to the file
with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)

print(f"Updated JSON saved to {file_path}")