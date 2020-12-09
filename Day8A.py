def load(filename):
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(filename) as in_file:
            loaded_txt = in_file.read().strip().split("\n")
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, filename))

def been_here(i, visited):
    if i in visited:
        return True
    return False

inputdata = load('Day8A-input.txt')
instructions = [i.split(" ") for i in inputdata]
visited = set()
accumulator = 0
i = 0

while True:
    num = int(instructions[i][1])
    print(accumulator)
    if instructions[i][0] == "nop":
        i += 1
        if been_here(i, visited):
            break
        visited.add(i)
        continue
    elif instructions[i][0] == "acc":
        i += 1
        if been_here(i, visited):
            break
        visited.add(i)
        accumulator += num
        continue
    else:
        i += num
        if been_here(i, visited):
            break
        visited.add(i)

print(accumulator)        