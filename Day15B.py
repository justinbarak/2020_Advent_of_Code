# import matplotlib.pyplot as plt
# import re
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


# input_list = load("Day15A-testinput.txt")
input_list = [2,0,1,9,5,19]
# input_list = [3,2,1]
final_number = 30_000_000
last_word = input_list[-2]
next_word = input_list[-1]
records = dict()
for i, num in enumerate(input_list[:len(input_list) - 1]):
    records[num] = i + 1
counter = len(records.keys())

while (counter < final_number):
    counter += 1
    if next_word in records.keys():
        last_word = next_word
        next_word = counter - records[next_word]
        records[last_word] = counter
    else:
        last_word = next_word
        records[last_word] = counter
        next_word = 0


    if (counter) % 1_000_000 == 0:
        print(format(counter / final_number * 100,".1f"),"%")


# key = next(key for key, value in records.items() if value == counter)

print(last_word)

