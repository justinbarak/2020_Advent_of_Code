import math

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
                if row >= len(inputlist)-1:
                    break
            if temp != "":
                outputlist.append(temp)
            if temp == "":
                row += 1
    except IndexError:
        pass
    return outputlist


fields_expected = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
fields_required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

inputtext = load("Day4A-input.txt")
parsed = list_combine(inputtext)
approved = 0

print(f"Total Passport Count: {len(parsed)}\n")

for line in parsed:
    temp = 0
    for item in fields_required:
        if item in line:
            temp += 1
    if temp == 7:
        approved +=1


print(f'Valid Passport Count: {approved}\n')