from importing_data_from_json_file_into_a_variable import data_2

test = data_2

def locate_card(cards, query):
    position = 0
    while True:
        if cards[position] == query:
            return position
        position += 1
        if position == len(cards):
            return -1
        

locate_card(**test['input']) == test['output']
locate_card(test["input"]["cards"], test["input"]["query"]) == test["output"]
print(test["input"]["cards"])
