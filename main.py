from importing_data_from_json_file_into_a_variable import data_2

test = data_2

def locate_card(cards, query):
    pass

locate_card(**test['input']) == test['output']
locate_card(test["input"]["cards"], test["input"]["query"]) == test["output"]
print(test["input"]["cards"])
