import pprint
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
    for bit, mask_bit in zip(bits, mask):
        if mask_bit == '0':
            masked.append(int(bit))
        elif mask_bit == '1':
            masked.append(1)
        elif mask_bit == 'x':
            masked.append('x')
        else:
            raise NotImplementedError
    return masked

def generate_options(in_mask: list) -> list:
    options = []
    mask = copy.deepcopy(in_mask)
    for i, bit in enumerate(mask):
        if bit == "x":
            optionAB = [mask[:i] + [0] + mask[i + 1:], mask[:i] + [1] + mask[i + 1:]]
            for j, optionA in enumerate(optionAB):
                if i >= 35:
                    temp = []
                    for j_bit in optionA:
                        temp.append(int(j_bit))
                    options.append(temp)
                    if j == len(optionAB)-1:
                        break
                else:
                    for returned_option in generate_options(optionA):
                        options.append(returned_option)
            return options
        elif i >= 35:
            return [mask]
    return mask

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
    masks = [0 for _ in range(36)]

    for line in instructions_list:
        mask_match = mre.match(line)
        if mask_match != None:
            mask = [x for x in mask_match.group('mask')]
            continue
        else:
            mem_match = ire.match(line)
            mem = mem_match.group('mem')
            mem_as_36bit = map_to_36bit(int(mem))
            decimal = int(mem_match.group('decimal'))
            # apply mask, leaving Xs, then generate options
            mem_masked = apply_mask(mask, mem_as_36bit)
            all_floaters = generate_options(mem_masked)
            for option in all_floaters:
                mem_write = count_36bit(option)
                memory_bank[mem_write] = decimal
            continue
    return memory_bank


input_list = load("Day14A-input.txt")
memory = (process_instructions(input_list))
total = 0
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(memory)
for location in memory:
    total += memory[location]
print(format(total,","))