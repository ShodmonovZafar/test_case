import random
from jovian.pythondsa import evaluate_test_case
from main import locate_card
from importing_data_from_json_file_into_a_variable import data_2
"""
Constraints:
    1 <= cards.length <= 10
    0 <= cards[i], query <= 100
    All the integers in nums are unique.
    nums is sorted in ascending order.
"""
cards_length_max = 10
cards_length_min = 1

cards_i_min = target_min = 0
cards_i_max = target_max = 100

cards = []
population = list(range(cards_i_min, cards_i_max + 1))

for i in range(10):
    list_one = random.sample(population, random.randint(cards_length_min, cards_length_max))
    list_one.sort()
    cards.append(list_one)

# target = random.randint(target_min + 1, target_max - 1)
j = 0
# for i in cards:
#     print("cards: ", i)
#     if j < 8:
#         x = random.choice(i)
#         print("query: ", x)
#         result = locate_card(i, x)
#     else:
#         x = random.randint(target_min + 1, target_max - 1)
#         print("query: ", x)
#         result = locate_card(i, x)
#     print(result)
#     j += 1
#     print()
# # tests = []
print(evaluate_test_case(locate_card, data_2))


