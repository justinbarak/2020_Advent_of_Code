import copy

def load(filename: str) -> list:
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(filename) as in_file:
            loaded_txt = in_file.read().strip().split("\n")
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, filename))

def seat_fill(input_list: list) -> list:
    input_list = copy.deepcopy(input_list)
    mod_list = copy.deepcopy(input_list)
    for i, row in enumerate(input_list):
        for j, seat in enumerate(row):
            min_i = 0
            max_i = len(input_list) - 1
            min_j = 0
            max_j = len(row) - 1
            if seat == ".":
                continue
            elif seat == "l":
                assert input_list[i][j] == seat
                matched = False
                for i_mini in range(max(min_i, i - 1), min(max_i, i + 1) + 1):
                    for j_mini in range(max(min_j, j - 1), min(max_j, j + 1) + 1):
                        if i_mini == i and j_mini == j: continue
                        if (input_list[i_mini][j_mini] == "#"):
                            matched = True
                            break
                if matched:
                    continue
                else:
                    mod_list[i] = mod_list[i][:j] + "#" + mod_list[i][j + 1:]
            elif seat == "#":
                count = 0
                assert input_list[i][j] == seat
                for i_mini in range(max(min_i, i - 1), min(max_i, i + 1) + 1):
                    for j_mini in range(max(min_j, j - 1), min(max_j, j + 1) + 1):
                        if i_mini == i and j_mini == j: continue
                        if (input_list[i_mini][j_mini] == "#"):
                            count += 1
                if count < 4:
                    continue
                else:
                    mod_list[i] = mod_list[i][:j] + "l" + mod_list[i][j + 1:]
            else:
                raise "Condition Not Anticipated"
    return mod_list

input_list = load("Day11A-input.txt")
once = copy.deepcopy(seat_fill(input_list))
twice = copy.deepcopy(seat_fill(once))

while once != twice:
    once = seat_fill(twice)
    twice = seat_fill(once)

count = 0
for row in twice:
    for char in row:
        if char == "#":
            count += 1
print(count)

