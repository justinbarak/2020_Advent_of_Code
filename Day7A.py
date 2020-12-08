import re

total_recursions = 0


def load(filename):
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(filename) as in_file:
            loaded_txt = in_file.read().strip().split("\n")
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, filename))

def list_analyze(inputlist):
    """Break list apart as required"""
    mainbag = dict()
    # mainbag = {main_bag: {1: {inner_bag: XX, num: YY}, ...}}
    reg = re.compile(r'(?P<main>\w+\s\w+\b)')
    reg_inner = re.compile(r'((?P<inner_digit>\d+)\s?(?P<inner>\w+\s\w+\b))')
    for line in inputlist:
        a, b = line.split(" bags contain ")
        matcha = reg.match(a)
        this_main = matcha.group('main')
        mainbag[this_main] = {}
        b_split = list(b.split(', '))
        matchb = reg_inner.search(b_split[0])
        if matchb == None:
            mainbag[this_main][1] = {}
            mainbag[this_main][1]['inner_bag'] = None
            mainbag[this_main][1]['num'] = 0
            continue
        # continuing below only if there are matches...
        for i in range(len(b_split)):
            matchb = reg_inner.search(b_split[i])
            inner_bag = matchb.group('inner')
            inner_digit = matchb.group('inner_digit')
            mainbag[this_main][i + 1] = {}
            mainbag[this_main][i + 1]['inner_bag'] = inner_bag
            mainbag[this_main][i + 1]['num'] = inner_digit
    return mainbag

inputdata = load('Day7A-input.txt')
all_bags = list_analyze(inputdata)
shiny_bags = set()
dull_bags = set()

def recurse_for_what(lookup_bag):
    # Declare global variables
    global total_recursions
    global shiny_bags
    global dull_bags
    global all_bags

    total_recursions += 1
    assert lookup_bag in all_bags.keys()
    if 'shiny gold' in all_bags[lookup_bag].values() or lookup_bag == 'shiny gold':
        shiny_bags.add(lookup_bag)
        return True
    if lookup_bag in shiny_bags:
        return True
    elif lookup_bag in dull_bags:
        return False
    for i in range(len(all_bags[lookup_bag])):
        inner_bag = all_bags[lookup_bag][i + 1]['inner_bag']
        if inner_bag == None:
            continue
        elif recurse_for_what(inner_bag) == True:
            shiny_bags.add(lookup_bag)
            return True
    dull_bags.add(lookup_bag)
    return False


assert recurse_for_what('shiny gold') == True
shiny_bags.add('shiny gold')


for k in all_bags.keys():
    recurse_for_what(k)

#ignore shiny gold, since it doesn't contain itself
print("Bags Containing shiny gold: ",len(shiny_bags)-1)
print("total recursions: ",total_recursions)