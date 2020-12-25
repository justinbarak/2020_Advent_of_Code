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

def min_max_in_dimension(active_points: set, dimension: int) -> int:
    # dimension 0 = x, 1 = y, 2 = z, 3 = w
    max_int = 0
    min_int = 0
    for point in active_points:
        max_int = max(max_int, point[dimension])
        min_int = min(min_int, point[dimension])
    return min_int, max_int

def cycle(active_points):
    # output
    points = set()
    # for each point from active min - 1 to max - 1 in each dimension
    min_x, max_x = min_max_in_dimension(active_points, 0)
    min_y, max_y = min_max_in_dimension(active_points, 1)
    min_z, max_z = min_max_in_dimension(active_points, 2)
    min_w, max_w = min_max_in_dimension(active_points, 3)

    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            for z in range(min_z - 1, max_z + 2):
                for w in range(min_w - 1, max_w + 2):
                    active_neighbors = 0
                    # count active neighbors
                    for x_n in range(x - 1, x + 2):
                        for y_n in range(y - 1, y + 2):
                            for z_n in range(z - 1, z + 2):
                                for w_n in range(w - 1, w + 2):
                                    if (x_n == x) and (y_n == y) and (z_n == z) and (w_n == w):
                                        # don't count yourself
                                        continue
                                    elif tuple([x_n, y_n, z_n, w_n]) in active_points:
                                        active_neighbors += 1
                                    else:
                                        # This means point in surroundings is not an active neighbor
                                        continue
                    # determine this points state given neighbor activity...
                    if (tuple([x, y, z, w]) in active_points) and (2 <= active_neighbors <= 3):
                        points.add(tuple([x, y, z, w]))
                    elif active_neighbors == 3:
                        points.add(tuple([x, y, z, w]))
    return points

def print_points(points: set):
    # for each point from active min to max in each dimension
    min_x, max_x = min_max_in_dimension(points, 0)
    min_y, max_y = min_max_in_dimension(points, 1)
    min_z, max_z = min_max_in_dimension(points, 2)
    min_w, max_w = min_max_in_dimension(points, 3)
    
    for w in range(min_w, max_w + 1):
        for z in range(min_z, max_z + 1):
            print(f'z={z}, w={w}')
            for y in range(min_y, max_y + 1):
                row = ''
                for x in range(min_x, max_x + 1):
                    if tuple([x, y, z, w]) in points:
                        row += '#'
                    else:
                        row += '.'
                print(row)
    print('\n')

file_list = load('Day17A-input.txt')

# . is inactive and # is active state for each point
points = set()
'''
points = set((x, y, z, w), ....) when "active",
    "inactive" points are not listed
'''
# initialize starting points
for j, row in enumerate(file_list):
    for i, column in enumerate(row):
        if column == "#":
            points.add(tuple([i, j, 0, 0]))
        elif column == ".":
            pass
        else:
            raise NotImplementedError

boot_cycles = 6
print_points(points)
for cyc in range(1, boot_cycles + 1):
    points = cycle(points)
    print_points(points)
    print(f'Total number of active points after cycle {cyc}: {len(points)}')