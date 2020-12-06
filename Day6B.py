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

def list_combine(inputlist):
    """Will take a list with blanks and multiple lines, cleanly separate
    into lines with all date to prepare to put in dictionary."""
    row = 0
    outputlist = []
    try:
        while row < len(inputlist):
            temp = ""
            while inputlist[row] != "":
                #search for next blank space, combine into temp vari and then write to list as 1 item
                temp += inputlist[row] + " "
                row += 1
                if row >= len(inputlist):
                    break
            if temp != "":
                outputlist.append(temp)
            if temp == "":
                row += 1
    except IndexError:
        pass
    return outputlist


inputdata = load('Day6A-input.txt')
combined = list_combine(inputdata)
total = 0

for line in combined:
    aset = set()
    bset = set()
    j = 0
    while aset == None:
        for i, char in enumerate(line):
            if char != " ":
                aset.add(char)
            if char == " ":
                j = i
                break
    i = j
    while i < len(line):
        char = line[i:i+1]
        if char != " ":
            bset.add(char)
        else:
            aset.intersection(bset)
            bset.clear
    total += len(aset)

print(total)
print(combined[-1])