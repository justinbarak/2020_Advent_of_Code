
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

def op(string_in: str) -> str:
    str_mod = string_in.split(' ')
    while len(str_mod) > 1:
        if '+' in str_mod:
            index = str_mod.index("+")
            a = int(str_mod[index - 1])
            b = int(str_mod.pop(index + 1))
            op = str_mod.pop(index)
            str_mod[index - 1] = a + b
        else:
            a = int(str_mod[0])
            b = int(str_mod.pop(2))
            op = str_mod.pop(1)
            output = 0
            if op == '*':
                output = a * b
            else:
                raise NotImplementedError
            # modify string
            str_mod[0] = output
    return str(str_mod[0])



# Quick idea, use regex to identify innermost parenthesis
# Break into little list bits to solve better
# replace parenthesis section with answer
# Repeat as needed until no parenthesis
# Repeat left to right solution once more until entire expression is solved

# Parenthesis Regex
par = re.compile(r'\((?P<par>\d+(?:\s.\s\d+)+)\)')
# Next operation Regex
oper = re.compile(r'(?P<a>\d+)\s(?P<op>.)\s(?P<b>\d+)')
chunk_to_op = re.compile(r'(\d+\s.\s\d+)')

homework_input = load('Day18A-input.txt')
homework_answer = []

# homework_input = ['2 * 3 + (4 * 5)']

for problem in homework_input:
    prepared_input_string = r'(' + problem + r')'
    calc_total = 0
    while calc_total == 0:
        res = par.findall(prepared_input_string)
        for parenthetical in res:
            reduced_string = op(parenthetical)
            prepared_input_string = prepared_input_string.replace(r'(' + parenthetical + r')', reduced_string)
        try:
            calc_total = int(prepared_input_string)
            homework_answer.append(calc_total)
        except:
            pass

print(sum(homework_answer))
