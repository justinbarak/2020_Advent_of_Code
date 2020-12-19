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

input_list = load("Day12A-input.txt")

parse = re.compile(r'(?P<alpha>\w)(?P<num>\d+)')

# east is 90, North is 0
direction = 90
# north is +, east is +
coord = [0,0]

for line in input_list:
    output = parse.match(line)
    a = output.group("alpha")
    num = int(output.group("num"))
    if a == "n":
        coord[0] += num
    elif a == "s":
        coord[0] -= num
    elif a == "e":
        coord[1] += num
    elif a == "w":
        coord[1] -= num
    elif a == "l":
        direction -= num
    elif a == "r":
        direction += num
    elif a == "f":
        if direction == 0:
            coord[0] += num
        elif direction == 180:
            coord[0] -= num
        elif direction == 90:
            coord[1] += num
        elif direction == 270:
            coord[1] -= num
    corr = direction // 360
    if direction >= 360:
        direction -= 360
    if direction < 0:
        direction += 360
        
print(coord)
print("man Dist: ", abs(coord[0]) + abs(coord[1]))
