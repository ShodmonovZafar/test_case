import json

data = {
    "foo": "bar",
    "alice": 1,
    "wonderland": [1, 2, 3]
}   

path_to_the_json_file = "json_files/json_file_1.json"

with open(path_to_the_json_file, 'w') as f:
    json.dump(data, f)
