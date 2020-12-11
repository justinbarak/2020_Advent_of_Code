def load(filename):
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(filename) as in_file:
            loaded_txt = in_file.read().strip().split("\n")
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, filename))

def finder_badone(preamble, input_list):
    i = 0
    preamble = int(preamble)
    while True:
        found = False
        input_preambled = input_list[i: i + preamble]
        next_item = input_list[i + preamble]
        for value1 in input_preambled:
            for value2 in input_preambled:
                if value1 == value2:
                    continue
                value1int = int(value1)
                value2int = int(value2)
                if int(next_item) - value1int == value2int:
                    found = True
                    break
            if found:
                break
        if not found:
            print("First Number Not Found: ", next_item)
            return next_item
        i += 1

def finder_contigsum(sum_target, input_list):
    i = 0
    while True:
        j = 1
        input_trunc = input_list[i: i + j]
        sum_slice = sum(input_trunc[:])
        while sum_slice < sum_target:
            input_trunc = input_list[i: i + j]
            sum_slice = sum(input_trunc[:])
            if sum_slice == sum_target:
                print("List of Consecutive Numbers: ", input_trunc)
                return input_trunc
            j += 1

        i += 1


input_list = load("Day9A-input.txt")
input_int = list(map(int, input_list))
preamble = 25

weakness = int(finder_badone(preamble, input_list))
consecutive_list = finder_contigsum(weakness, input_int)

min_num = min(consecutive_list)
max_num = max(consecutive_list)
print("Min: ",min_num)
print("Max: ",max_num)
print("Sum of Min & Max", min_num + max_num)
