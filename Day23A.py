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

def split_cups_str(cup_str: list) -> list:
    cup_lst = []
    for row in cup_str:
        for character in row:
            cup_lst.append(int(character))
    return cup_lst

def move(cups: list, current_cup: int) -> list:
    cups = copy.deepcopy(cups)
    print(f'current cup: {current_cup}')
    print(f"cups: {' '.join(str(x) for x in cups)}")
    # Choose next 3 cups in clockwise
    current_cup_index = cups.index(current_cup)
    pick_up = []
    if current_cup_index + 3 < len(cups):
        for _ in range(1,4):
            pick_up.append(cups.pop(current_cup_index + 1))
    else:
        front_loops = (len(cups) - current_cup_index)
        for _ in range(1, front_loops):
            pick_up.append(cups.pop(current_cup_index + 1))
        for _ in range(0, 4 - front_loops):
            pick_up.append(cups.pop(0))
    # 3 cups are removed
    print(f"pick up: {' '.join(str(x) for x in pick_up)}")
    # select destination cup
    destination_cup = current_cup - 1
    while destination_cup not in cups:
        destination_cup -= 1
        if destination_cup < 1:
            destination_cup = 9
    # destination cup now selected
    print(f"destination: {destination_cup}")
    destination_index = cups.index(destination_cup)
    # insert
    while len(pick_up) > 0:
        cups.insert(destination_index + 1, pick_up.pop(-1))
    if current_cup == cups[-1]:
        next_cup = cups[0]
    else:
        next_cup = cups[cups.index(current_cup) + 1]
    return cups, next_cup

# cups_str = load('Day23A-testinput.txt')
cups_str = ['215694783']
cup_list = split_cups_str(cups_str)
next_cup = cup_list[0]
for move_num in range(1,101):
    print(f'\n-- move {move_num} --')
    cup_list, next_cup = move(cup_list, next_cup)

print(cup_list)
