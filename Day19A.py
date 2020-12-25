
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

input_list = load('Day19A-input.txt')

rules = list()
messages = list()
i = 0
j = 0

# Put input lists into appropriate lists
while i < len(input_list):
    if j == 0:
        if input_list[i] == '':
            j = 1
            i += 1
            continue
        rules.append(input_list[i])
    if j > 0:
        messages.append(input_list[i])
    i += 1

# Put rules into the right order, where they don't reference an
# unmentioned rule
gen_rule_parse = re.compile(r'(?P<x>\d+): (?P<y>.*)')
str_rule_parse = re.compile(r'(?P<x>\d+): (?P<y>"\w")')

mentioned_rules = set()
all_chars = dict()
all_rules = dict()
zero_rule = ""
i = 0
# first pull out all single characters and zero
while i < len(rules):
    rule = rules[i]
    str_rule = str_rule_parse.match(rule)
    if str_rule != None:
        rules.pop(i)
        num = str_rule.group('x')
        char = str_rule.group('y')
        all_chars[int(num)] = char
        mentioned_rules.add(int(num))
    elif zero_rule == "":
        z_rule = gen_rule_parse.match(rule)
        if z_rule.group('x') == '0':
            rules.pop(i)
            mentioned_rules.add(int(0))
            zero_rule = z_rule.group('y')
        else:
            i += 1
    else:
        i += 1

# pull all other rules
for rule in rules:
    p_rule = gen_rule_parse.match(rule)
    all_rules[p_rule.group('x')] = p_rule.group('y')

# Compile nested rules into a single regex
rules_dict = dict()

# clean characters first
for k, rule in all_chars.items():
    assert r'"' in rule
    cleaned_rule = rule.replace(r'"', '')
    rules_dict[k] = cleaned_rule

# now for messy rules, skipping rules which do not have all sub rules yet parsed
i =  0
target = len(all_chars) + len(rules) + 1
while len(mentioned_rules) < target:
    for k, rule in zip(list(all_rules.keys()), list(all_rules.values())):
        nums = rule.split(' ')
        substituted = []
        good_to_go = True
        for num in nums:
            if (num != r'|') and (int(num) not in mentioned_rules):
                good_to_go = False
        if good_to_go == False:
            i += 1
            continue
        for num in nums:
            if num == r'|':
                substituted.append(r'|')
            else:
                loc = str(rules_dict[int(num)])
                substituted.append(loc)
        rules_dict[int(k)] = '(' + ''.join(substituted) + ')'
        mentioned_rules.add(int(k))
        del all_rules[k]
    if i > len(all_rules):
        i = 0

# now for final 0
nums = zero_rule.split(' ')
substituted = []
for num in nums:
    if num == r'|':
        substituted.append(r'|')
    else:
        loc = str(rules_dict[int(num)])
        substituted.append(loc)
rules_dict[0] = '(' + ''.join(substituted) + ')'


final_rule = r'^' + rules_dict[0] + r'$'

print(final_rule)

final_regex = re.compile(final_rule)

# Examine every item
message_good = 0
for message in messages:
    analysis = final_regex.match(message)
    if analysis != None:
        message_good += 1

print('Good messages: ',message_good)