import copy

def load(filename):
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(filename) as in_file:
            loaded_txt = in_file.read().strip().split("\n")
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, filename))

input_list = load("Day10A-input.txt")
input_int = list(map(int, input_list))

input_int.sort()
orig_list = copy.deepcopy(input_int)
input_int.insert(0,0)
orig_list.append(max(input_int[:]) + 3)
deltas = []
ones = 0
threes = 0
for a, b in zip(orig_list, input_int):
    deltas.append(a - b)
    if deltas[-1] == 1:
        ones += 1
    elif deltas[-1] == 3:
        threes += 1
print(ones * threes)