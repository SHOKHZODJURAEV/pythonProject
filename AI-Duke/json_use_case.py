import json

# Python dictionary
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
# Convert dictionary to JSON string
json_str = json.dumps(data)
print(json_str)

json_string = '{"name": "Alice", "age": 25, "city": "New York"}'

# Convert JSON string to Python dictionary
python_data = json.loads(json_string)
print(python_data["name"])  # Output: Alice

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

with open("data.json", "r") as file:
    loaded_data = json.load(file)

print(loaded_data)


