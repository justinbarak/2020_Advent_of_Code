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

input_list = load("Day13A-input.txt")

time_target = int(input_list[0])
buses = []
feed = input_list[1].split(",")
for item in feed:
    if item != 'x':
        buses.append(int(item))

time = time_target
first_bus = []
while True:
    for bus in buses:
        if time % bus == 0:
            first_bus.append(bus)
            break
    if len(first_bus) > 0:
        break
    else:
        time += 1

print("Bus: ",first_bus)
print("Time: ", time - time_target)
print("Answer: ", (time - time_target) * first_bus[0])