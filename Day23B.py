import copy
import re

def load(filename: str) -> list:
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(filename) as in_file:
            loaded_txt = in_file.read().strip().split("\n")
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, filename))

def split_cups_str(cup_str: list) -> dict:
    # dict{number: next_number in order}
    cup_dict = dict()
    cup_list = [int(x) for x in cup_str[0]]
    cup_list_p = cup_list[1:] + [cup_list[0]]
    cup_dict = dict(zip(cup_list, cup_list_p))
    return cup_dict

def move(cups: dict, current_cup: int) -> int:
    # print(f'current cup: {current_cup}')
    # print(f"cups: {' '.join(str(x) for x in cups)}")
    # Choose next 3 cups in clockwise
    pick_up = []
    pick_up.append(cups[current_cup])
    pick_up.append(cups[pick_up[-1]])
    pick_up.append(cups[pick_up[-1]])
    # stitch up around "removed" cups
    cups[current_cup] = cups[pick_up[-1]]
    # 3 cups are "removed"
    # print(f"pick up: {' '.join(str(x) for x in pick_up)}")
    # select destination cup
    destination_cup = current_cup - 1
    while destination_cup in pick_up:
        destination_cup -= 1
    if destination_cup < 1:
        destination_cup = max(cups.keys())
    # destination cup now selected
    # print(f"destination: {destination_cup}")
    # insert and restitch in new 3 numbers
    temp = cups[destination_cup]
    cups[destination_cup] = pick_up[0]
    cups[pick_up[-1]] = temp
    next_cup = cups[current_cup]
    return next_cup

# cups_str = load('Day23A-testinput.txt')
cups_str = ['215694783']
next_cup = int(cups_str[0][0])
last_cup = int(cups_str[0][-1])
cup_dict = split_cups_str(cups_str)
for i in range(10,1_000_001):
    cup_dict[i] = i + 1
cup_dict[1_000_000] = next_cup
cup_dict[last_cup] = 10
number_of_loops = 10_000_000
for move_num in range(1, number_of_loops + 1):
    # print(f'\n-- move {move_num} --')
    if move_num % 1_000_000 == 0:
        print(f'Move % Completed: {round(move_num / number_of_loops * 100)}')
    next_cup = move(cup_dict, next_cup)
desired_nums = []
desired_nums.append(cup_dict[1])
desired_nums.append(cup_dict[desired_nums[-1]])
print("Final Numbers:", desired_nums)
print(f"Answer: {desired_nums[0] * desired_nums[1]}")
