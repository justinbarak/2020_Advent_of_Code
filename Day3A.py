import re

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

inputtext = load("Day3A-input.txt")

row = 0
col = 0
tree = 0
maxcol = len(inputtext[1])
maxrow = len(inputtext)

while row < maxrow:
    if inputtext[row][col] == r'#':
        tree += 1
    row += 1
    col += 3
    if col > maxcol-1:
        col = col - maxcol
# print(f"Row:{row}, Col:{col}")
print(tree)