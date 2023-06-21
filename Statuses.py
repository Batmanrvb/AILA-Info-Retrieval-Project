import os

statutes_folder = r"C:\Users\Raj Vikrant Brahma\Desktop\cases_folder\Object_statutes"

#Read the statute information from text files
statutes_data = []

# Iterate over the text files in the statutes folder
for file_name in os.listdir(statutes_folder):
    file_path = os.path.join(statutes_folder, file_name)
    with open(file_path, 'r', encoding='utf-8') as file:
        statute_title = file.readline().strip()
        statute_description = file.read().strip()
        statutes_data.append({'title': statute_title, 'description': statute_description})

#Perform your task (e.g., retrieval or classification) using the statutes_data

for statute in statutes_data:
    print(statute['title'])
    print(statute['description'])
    print()

