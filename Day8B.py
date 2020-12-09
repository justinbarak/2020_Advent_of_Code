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

def been_here(i, visited):
    prior_visit = visited[:len(visited) - 1]
    if i in prior_visit:
        return True
    return False

def hit_target(i):
    global target
    if i == target:
        return True
    return False

def loopcheck(visited, accum, instruct, altered):

    i = visited[-1]
    accumulator = copy.deepcopy(accum)
    instructions = copy.deepcopy(instruct)
    if hit_target(i):
        print('Accumulator value at end: ',sum(accumulator[:]))
        return True
    num = int(instructions[i][1])
    # check if I've visited this location before, i.e. loop stuck
    if been_here(i, visited):
        return False   

    if instructions[i][0] == "nop":
        visited.append(i + 1)
        accumulator.append(0)
    elif instructions[i][0] == "acc":
        visited.append(i + 1)
        accumulator.append(num)
    else:
        visited.append(i + num)
        accumulator.append(0)
    if loopcheck(visited, accumulator, instructions, altered) == False:
        if altered == True: return False
        #modify instructions and redo
        altered = True
        visited.pop()
        accumulator.pop()
        if instructions[i][0] == "nop":
            instructions[i][0] = "jmp"
        elif instructions[i][0] == "acc":
            return False
        else:
            instructions[i][0] = "nop"
        # replan next step
        if instructions[i][0] == "nop":
            visited.append(i + 1)
            accumulator.append(0)
        elif instructions[i][0] == "acc":
            visited.append(i + 1)
            accumulator.append(num)
        else:
            visited.append(i + num)
            accumulator.append(0)        
        
        if loopcheck(visited, accumulator, instructions, altered) == False:
            return False
        else: return True
    else: return True
    


assert been_here(1, [0,1,2]) == True
assert been_here(2, [1,0,2]) == False

inputdata = load('Day8A-input.txt')
instructions = [i.split(" ") for i in inputdata]
visited = [0]
accumulator = [0]
target = len(instructions)

loopcheck(visited, accumulator, instructions, False)
     