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

inputtext = load("Day2A-input.txt")
validpasswords = 0
reggie = re.compile(r'((?P<min>\d{1,2})-(?P<max>\d{1,2})\s(?P<character>\w):\s(?P<password>\w+))')

for line in inputtext:
    matched = reggie.match(line)
    mini = int(matched.group('min'))
    maxi = int(matched.group('max'))
    character = matched.group('character')
    password = matched.group('password')
    match1 = bool(password[mini-1] == character)
    match2 = bool(password[maxi-1] == character)
    if ((match1 or match2) and not (match1 and match2)) :
        validpasswords +=1

print(validpasswords)