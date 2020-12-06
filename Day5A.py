import itertools

def load(filename):
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(filename) as in_file:
            loaded_txt = in_file.read().strip().split("\n")
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, filename))


# 0 -> 127
FB = [64, 32, 16, 8, 4, 2, 1]
LR = [4, 2, 1]
inputtext = load("Day5A-input.txt")
max_seatID = 0

for line in inputtext:
    #calc row
    tempFBstr = line[:7]
    row = 0
    for i, char in enumerate(tempFBstr):
        if char == 'b':
            row += FB[i] 
    #calc col
    tempFBstr = line[7:]
    col = 0
    for i, char in enumerate(tempFBstr):
        if char == 'r':
            col += LR[i]     
    #calc seatID
    seatID = row * 8 + col
    if seatID > max_seatID:
        max_seatID = seatID
print(max_seatID)
