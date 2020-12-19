# import matplotlib.pyplot as plt
import re
import copy

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

def validate_ticket(rules: dict(), ticket: list) -> int:
    errors = 0
    invalids = set()
    for number in ticket:
        number = int(number)
        any_valid = False
        for rule in rules:
            a = int(rules[rule][1])
            b = int(rules[rule][2])
            c = int(rules[rule][3])
            d = int(rules[rule][4])
            if ((a <= number <= b) or (c <= number <= d)):
                any_valid = True
        if not(any_valid):
            invalids.add(number)
    if len(invalids) > 0:
        errors = sum(invalids)
    return errors

input_list = load("Day16A-input.txt")
rules, my_ticket, nearby = parse_input(input_list)

error_rate = 0
for ticket in nearby:
    error_rate += validate_ticket(rules, ticket)

print(error_rate)
