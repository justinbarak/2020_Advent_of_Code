
import regex
import copy
import functools

def load(filename: str) -> list:
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(filename) as in_file:
            loaded_txt = in_file.read().strip().split("\n")
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, filename))

class tile:
    """
    Tile of image, will overlap with another neighbor along edge for 1 character
    """
    def __init__(self, lists, num):
        """
        Input lists must be a list of lists
        """
        self.image = copy.deepcopy(lists)
        self.name = num
        self.match_counter = 0

    def __str__(self):
        s = f'Tile Number: {self.name}\n'
        t = ''
        for row in self.image:
            t += f'{str(row[:])}\n'
        return s + t

    def flip_y(self):
        """Flip across the horizontal axis"""
        output = []
        y = len(self.image[0])
        for i in range(y - 1, -1, -1):
            output.append(self.image[i][:])
        self.image = output

    def flip_x(self):
        """Flip across the vertical axis"""
        output = []
        for row in self.image:
            output.append(row[::-1])
        self.image = output

    def rotate(self):
        """Rotate Right Once"""
        self.image = [str(''.join(row)) for row in zip(*reversed(self.image))]

    def sides(self):
        """Return all 4 side boundaries starting from Up[0] and going counter-clockwise"""
        side_list = []
        options = ['a','b','c','d']
        for _ in range(4):
            side_list.append(self.image[0])
            self.rotate()
        return dict(zip(options, side_list))
    
    def add_match_counter(self):
        self.match_counter += 1

input_list = load('Day20A-input.txt')
input_list.append("")
tile_num_scan = regex.compile(r'tile (?P<num>\d*):')
tile_num = ''
tiles = []
temp_tile = []
for line in input_list:
    if str(line).startswith('tile'):
        scan = tile_num_scan.match(line)
        tile_num = scan.group('num')
    elif str(line) == '':
        # do wrap up stuff for this tile
        tiles.append(tile(temp_tile, tile_num))
        temp_tile.clear()
    else:
        temp_tile.append(line)

all_sides = dict()
for this_tile in tiles:
    sides = this_tile.sides()
    all_sides[int(this_tile.name)] = sides

matches = dict()
paired = set()
for tile_num in all_sides.keys():
    for letter, side in all_sides[tile_num].items():
        if (tile_num, letter) in paired:
            continue
        for tile_num_2 in all_sides.keys():
            for letter_2, side_2 in all_sides[tile_num_2].items():
                if tile_num == tile_num_2 and letter == letter_2:
                    continue
                elif side == side_2[::-1] or side == side_2:
                    if tile_num not in matches:
                        matches[tile_num] = {}
                    if tile_num_2 not in matches:
                        matches[tile_num_2] = {}
                    matches[tile_num][letter]= {tile_num_2: letter_2}
                    paired.add((tile_num_2, letter_2))
                    if 'match_counter' not in matches[tile_num]:
                        matches[tile_num]['match_counter'] = 0
                    matches[tile_num]['match_counter'] += 1
                    if 'match_counter' not in matches[tile_num_2]:
                        matches[tile_num_2]['match_counter'] = 0
                    matches[tile_num_2]['match_counter'] += 1
        
# find corners, where matches = 2
corners = []
for tiles in matches:
    if matches[tiles]['match_counter'] == 2:
        corners.append(tiles)

total = functools.reduce(lambda x,y: x*y, corners)

print(matches)

print(total)
