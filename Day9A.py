def load(filename):
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(filename) as in_file:
            loaded_txt = in_file.read().strip().split("\n")
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, filename))

def finders(preamble):
    i = 0
    while True:
        input_preambled = inputtext[i: i + preamble]
        next_item = inputtext[i + preamble]
        found = False
        for value1 in input_preambled:
            for value2 in input_preambled:
                if value1 == value2:
                    continue
                value1int = int(value1)
                value2int = int(value2)
                if int(next_item) - value1int == value2int:
                    found = True
                if found:
                    break
            if found:
                break
        if not found:
            print("First Number Not Found: ", next_item)
            return next_item
        i += 1
    return False

inputtext = load("Day9A-input.txt")
preamble = 25
finders(preamble)