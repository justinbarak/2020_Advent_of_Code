# import matplotlib.pyplot as plt
import re
import copy
from Day16A import validate_ticket

def load(filename: str) -> list:
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(filename) as in_file:
            loaded_txt = in_file.read().strip().split("\n")
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, filename))

def parse_input(input_list: list) -> list:
    rules = dict()
    my_ticket = []
    nearby = []
    rerules = re.compile(r'(?P<rule_name>.*?): (?P<rule_1a>\d+)-(?P<rule_1b>\d+) or (?P<rule_2a>\d+)-(?P<rule_2b>\d+)')
    rows = 0
    while input_list[rows] != "":
        scanrule = rerules.match(input_list[rows])
        if scanrule == None: break
        rules[scanrule.group('rule_name')] = {
            1: scanrule.group('rule_1a'),
            2: scanrule.group('rule_1b'),
            3: scanrule.group('rule_2a'),
            4: scanrule.group('rule_2b')
            }
        rows += 1
    rows += 2
    my_ticket = input_list[rows].split(",")
    rows += 3
    for ticket in input_list[rows:]:
        nearby.append(ticket.split(","))
    return rules, my_ticket, nearby

def itemize_ticket(rules: dict(), tickets: list, match_options = "") -> list:
    corresponding_fields = dict()
    rules = copy.deepcopy(rules)
    if match_options == "":
        match_options = set(range(len(tickets[0][0])))
    temp_matches = list()
    rule = list(rules.keys())
    for rule in rules:
        temp_matches.clear()
        a = int(rules[rule][1])
        b = int(rules[rule][2])
        c = int(rules[rule][3])
        d = int(rules[rule][4])
        for i in match_options:
            true_for_pos = True
            for ticket in tickets:
                number = ticket[0][i]
                number = int(number)
                if not((a <= number <= b) or (c <= number <= d)):
                    true_for_pos = False
            if true_for_pos:
                temp_matches.append([rule, i])
        if len(temp_matches) == 1:
            corresponding_fields[temp_matches[0][0]] = temp_matches[0][1]
    return corresponding_fields

def loop_tickets(rules: dict(), tickets: list, match_options: set) -> list:
        rule_copied = copy.deepcopy(rules)
        solved = dict()
        while True:
            categories = itemize_ticket(rule_copied, tickets, match_options)
            print(f'{len(rule_copied.keys())} Solutions Remaining to Find')
            print("Solutions: ",solved)
            
            
            if len(categories.keys()) > 1:
                # This is when too many options work, pick the first and
                # recurse down, go to next if branch dies before solving all
                for k, v in categories.items():
                    rule_min = copy.deepcopy(rule_copied)
                    del rule_min[k]
                    match_min = copy.deepcopy(match_options)
                    match_min.discard(v)
                    soln = loop_tickets(rule_min, tickets, match_min)
                    if soln == None:
                        continue
                    else:
                        for k, v in soln.items():
                            solved[k] = v
                            match_options.discard(v)
                            del rule_copied[k]
                        return soln

            elif len(categories.keys()) == 1:
                # This is the standard operation
                # continue looking for next key
                for k, v in categories.items():
                    solved[k] = v
                    match_options.discard(v)
                    del rule_copied[k]
            else:
                # This happens when branch dies, no remaining solutions
                return None
            if len(rule_copied.keys()) == 0:
                return solved

input_list = load("Day16A-input.txt")
rules, my_ticket, nearby = parse_input(input_list)
comb_tickets = [my_ticket] + nearby
valid_tickets = list()
for ticket in nearby:
    if validate_ticket(rules, ticket) == 0:
        valid_tickets.append([ticket])
match_options = set(range(len(valid_tickets[0][0])))
solved = dict()
solved = loop_tickets(rules, valid_tickets, match_options)


print("Total Categories, should be 20... ",len(solved.keys()))
# split rules into only those rules that start with departure
dep_rules = dict()
for rule in solved.keys():
    if str(rule).startswith('depart'):
        dep_rules[rule] = solved[rule]
print(dep_rules)
# which numbers on my ticket correspond to these 6 categories
applied_nums = []
for rule in dep_rules:
    index_targ = int(dep_rules[rule])
    applied_nums.append(my_ticket[index_targ])
    
print(applied_nums)

# multiply these 6 numbers together
total = 1
for num in applied_nums:
    total *= int(num)
print(total)
