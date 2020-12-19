# import matplotlib.pyplot as plt
# import re
import copy
from typing import final

def load(filename: str) -> list:
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(filename) as in_file:
            loaded_txt = in_file.read().strip().split("\n")
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, filename))

def mem_game_response(last_response: int, history: list) -> int:
    if last_response in history[:len(history)-1]:
        backwards = history[::-1]
        most_recent = backwards.index(last_response)
        sub_backwards = backwards[most_recent + 1:]
        second_most_recent = sub_backwards.index(last_response) + most_recent + 1
        delta = abs(most_recent - second_most_recent)
        return delta
    else:
        return 0

# input_list = load("Day15A-testinput.txt")
input_list = [2,0,1,9,5,19]
# input_list = [0,3,6]
final_number = 30_000_000
game_list = copy.deepcopy(input_list)
last_word = game_list.pop()

while (len(game_list) < final_number):
    game_list.append(last_word)
    last_word = mem_game_response(last_word, game_list)
    if len(game_list) % 10_000 == 0:
        print(format(len(game_list) / final_number * 100,".3f"),"%")

index_list = list(range(len(game_list)))
print(game_list[-1])

# delta = copy.deepcopy([x-y for x, y in zip(game_list[:len(game_list)-1], game_list[1:])])

# plt.plot(index_list[1:], delta)
# plt.show()
