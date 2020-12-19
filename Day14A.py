import pprint
import re

def load(filename: str) -> list:
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(filename) as in_file:
            loaded_txt = in_file.read().strip().split("\n")
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, filename))

def map_to_36bit(decimal: int) -> list:
    converted = []
    for i in range(36)[::-1]:
        if decimal >= (2 ** i):
            converted.append(1)
            decimal -= 2 ** i
        else:
            converted.append(0)
    assert decimal == 0
    return converted

def apply_mask(mask, bits):
    masked = []
    for bit, char in zip(bits, mask):
        if char == 'x':
            masked.append(bit)
        else:
            masked.append(char)
    return masked

def count_36bit(input_36bit: list) -> int:
    running_total = 0
    for i, bit in enumerate(input_36bit):
        if int(bit) == 1:
            running_total += (2 ** (35 - i))
        else:
            continue
    return running_total

def process_instructions(instructions_list):
    mre = re.compile(r'mask = (?P<mask>\w{36})')
    ire = re.compile(r'mem\[(?P<mem>\w+)\] = (?P<decimal>\d*)')
    memory_bank = dict()
    mask = [0 for _ in range(36)]

    for line in instructions_list:
        mask_match = mre.match(line)
        if mask_match != None:
            mask = [x for x in mask_match.group('mask')]
            continue
        else:
            mem_match = ire.match(line)
            mem = mem_match.group('mem')
            decimal = int(mem_match.group('decimal'))
            dec_as_36bit = map_to_36bit(decimal)
            # mask bits
            dec_masked = apply_mask(mask, dec_as_36bit)
            memory_bank[mem] = dec_masked
            continue
    return memory_bank


input_list = load("Day14A-input.txt")
memory = (process_instructions(input_list))
total = 0
pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(memory)
for location in memory:
    total += count_36bit(memory[location])
print(total)