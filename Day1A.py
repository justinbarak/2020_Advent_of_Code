'''Sort out a list and find the 2 numbers that sum to 2020
and return their product
For Advent of Code 2020 Day 1A
'''

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
output = None

for value in inputtext:
    valueint = int(value)
    if str(2020 - valueint) in inputtext:
        output = valueint * (2020 - valueint)

print(output)