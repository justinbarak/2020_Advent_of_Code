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

def min_max_in_dimension(active_points, dimension):
    # dimension 0 = x, 1 = y, 2 = z
    max_int = None
    min_int = None
    for point in active_points:
        max_int = max(max_int, point[dimension])
        min_int = min(min_int, point[dimension])
    return min_int, max_int

def cycle(active_points):
    # copy base input to modify
    
    # for each point from active min - 1 to max - 1 in each dimension
    min_x, max_x = min_max_in_dimension(active_points, 0)
    min_y, max_y = min_max_in_dimension(active_points, 1)
    min_z, max_z = min_max_in_dimension(active_points, 2)

file_list = load('Day17A-testinput.txt')

# . is inactive and # is active state for each point
points = dict
'''
points = [[x, y, z, True], ....] when "active"
'''
