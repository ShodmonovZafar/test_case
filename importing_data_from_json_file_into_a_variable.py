import json

path_to_the_json_file = "json_files/json_file_2.json"

with open(path_to_the_json_file, 'r') as f:
    data_2 = json.load(f)


