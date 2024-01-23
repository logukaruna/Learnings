import json

import openpyxl

# Define the file path of your Excel (.xlsx) file
loc = 'D:\\Contacts.xlsx'

# Open the Excel workbook
wb = openpyxl.load_workbook(loc)

# Select the specific sheet by name ("contacts" in this case)
sheet = wb['contacts']

# Create an empty list to store the data
data = []

# Iterate through rows starting from the second row (skip header)
for row in sheet.iter_rows(min_row=2, values_only=True):
    name, number1, number2 = row
    entry = {
        'name': name,
        'number 1': number1,
        'number 2': number2,
    }
    data.append(entry)

# Convert the data list to a JSON string
json_data = json.dumps(data, indent=4)

json_file_path = 'D:\\Programming\\Learnings\\Python\\AI\\DB.json' 

# Save the JSON data to the JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print(f"JSON data has been saved to '{json_file_path}'")

# If you want to save the JSON data to a file, you can do:
# with open('output.json', 'w') as json_file:
#     json.dump(data, json_file, indent=4)
