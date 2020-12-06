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

treeproduct = 1

maxcol = len(inputtext[1])
maxrow = len(inputtext)
right = [1, 3, 5, 7, 1]
down = [1, 1, 1, 1, 2]

for across, slide in zip(right, down):
    tree = 0
    row = 0
    col = 0

    while row < maxrow:
        if inputtext[row][col] == r'#':
            tree += 1
        row += slide
        col += across
        if col > maxcol-1:
            col = col - maxcol
    treeproduct *= tree
    print(f"Right:{across}, Down:{slide}, total:{tree}\nRunning Total:{treeproduct}")
print('\n',treeproduct)