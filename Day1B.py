import sys

def load(filename):
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(filename) as in_file:
            loaded_txt = in_file.read().strip().split("\n")
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, filename))
        # sys.exit(1)

inputtext = load("Day1A-input.txt")
inputint = list(map(int, inputtext))
output = None

for value1 in inputint:
    for value2 in inputint:
        for value3 in inputint:
            if ((2020 - value1 - value2) == value3) and (value1 != value2 != value3):
                print(value1 * value2 * value3)
