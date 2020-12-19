from math import lcm

def load(filename: str) -> list:
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(filename) as in_file:
            loaded_txt = in_file.read().strip().split("\n")
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, filename))

# def lcm(a, b):
#     return abs(a * b) // gcd(a, b)

input_list = load("Day13A-input.txt")

buses = []
bus_t = []
# max_bus = [0, 0]
time = 0
current_lcm = 1
last_solution = 0

feed = input_list[1].split(",")
for i, item in enumerate(feed):
    if item != 'x':
        item = int(item)
        buses.append(item)
        bus_t.append(i)
        while True:
            if (time + i) % (item) == 0:
                bus_iter = (item)
                last_solution = time
                break
            time += current_lcm
        current_lcm = lcm(*buses[:])

        # if item > max_bus[0]:
        #     max_bus = [item, i]


# time = max_bus[0] + max_bus[1]
# while True:
#     match = True
#     for bus, t_shift in zip(buses, bus_t):
#         if (time + t_shift) % bus != 0:
#             match = False
#     if match == True:
#         break
#     else:
#         time += max_bus[0]

print("Time: ", format(last_solution, ","))