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

def rotate_left(coord: list) -> list:
    NS = coord[0]
    EW = coord[1]
    return [EW, -NS]

def rotate_right(coord: list) -> list:
    NS = coord[0]
    EW = coord[1]
    return [-EW, NS]


input_list = load("Day12A-input.txt")

parse = re.compile(r'(?P<alpha>\w)(?P<num>\d+)')

# north is +, east is +
coord = [0,0]
waypoint = [1, 10]

for line in input_list:
    output = parse.match(line)
    a = output.group("alpha")
    num = int(output.group("num"))
    if a == "n":
        waypoint[0] += num
    elif a == "s":
        waypoint[0] -= num
    elif a == "e":
        waypoint[1] += num
    elif a == "w":
        waypoint[1] -= num
    elif a == "l":
        times = num // 90
        for _ in range(times):
            waypoint = copy.deepcopy(rotate_left(waypoint))
    elif a == "r":
        times = num // 90
        for _ in range(times):
            waypoint = copy.deepcopy(rotate_right(waypoint))
    elif a == "f":
        coord = [coord[0] + waypoint[0] * num, coord[1] + waypoint[1] * num]
    # print("Ship Coord: ", coord)
    # print("Waypoint: ", waypoint)
    # print("\n")

        
print(coord)
print("man Dist: ", abs(coord[0]) + abs(coord[1]))
