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

def delta(lista, listb):
    """Subtracts 2 lists item by item, returns result as new list"""
    deltalist = []
    for a, b in zip(lista, listb):
        deltalist.append(abs( a - b))
    return deltalist

def delta_one(lista):
    return delta(lista[:len(lista)-1], lista[1:len(lista)])

def parse_for_ones(list_in):
    ones = 0
    list_out = []
    for item in list_in:
        if item == 1:
            ones += 1
            continue
        else:
            list_out.append(ones)
            ones = 0
    return list_out

input_list = load("Day10A-input.txt")
input_int = list(map(int, input_list))

input_int.sort()
input_int.insert(0,0)
input_int.append(max(input_int[:]) + 3)

deltas = delta_one(input_int)

parsed = parse_for_ones(deltas)

# dictionary of options
options = {
    0: 1,
    1: 1,
    2: 2,
    3: 4,
    4: 7
}

final_list = []
for num in parsed:
    final_list.append(options[num])

product = 1
for num in final_list:
    product *= num

print(product)