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
all_seatID = []

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
    all_seatID.append(seatID)

full_seatID = []
for i in range(128):
    for j in range(8):
        full_seatID.append(i*8 + j)

for seat in full_seatID:
    if seat not in all_seatID:
        if (seat + 8 in all_seatID) and (seat - 8 in all_seatID):
            print(seat)
