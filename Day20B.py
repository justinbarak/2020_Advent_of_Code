
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

    def __str__(self):
        s = f'Tile Number: {self.name}\n'
        t = ''
        for row in self.image:
            t += f'{str(row[:])}\n'
        return s + t

    def flip_y(self):
        """Flip across the horizontal axis"""
        output = []
        y = len(self.image)
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
    
    def strip_borders(self):
        temp = copy.deepcopy(self.image)
        length = len(temp)
        temp = temp[1: length - 1]
        output = []
        for line in temp:
            output.append(line[1: length - 1])
        return output

def find_tile_by_name(target:int, list_of_objects: list):
    i = 0
    while True:
        if int(list_of_objects[i].name) == target:
            return i
        else:
            i += 1

def rotate_nums(position_targ: int, current_position: int) -> int:
    if position_targ == current_position:
        return 0
    nums = list(range(4))
    for _ in range(position_targ):
        i = nums.pop()
        nums.insert(0, i)
    return int(nums[current_position])

def align_right(tile1: tile, tile2: tile):
    assert type(tile1) == type(tile2)
    # tile 1 is fixed in position...
    # tile 2 is mobile...
    col_to_match = tile1.sides()['d']
    base_options = list(tile2.sides().values())
    if col_to_match[::-1] in base_options:
        i = base_options.index(col_to_match[::-1])
        if i == 1: return None # matching col facing left
        i = rotate_nums(1, i)
        for _ in range(i):
            tile2.rotate()
        return None
    # now try flipping x and y
    tile2.flip_x()
    # tile2.flip_y()
    base_options = list(tile2.sides().values())
    if col_to_match[::-1] in base_options:
        i = base_options.index(col_to_match[::-1])
        if i == 1: return None # matching col facing left
        i = rotate_nums(1, i)
        for _ in range(i):
            tile2.rotate()
        return None
    raise AttributeError("Could not make tiles match up")

def align_down(tile1: tile, tile2: tile):
    assert type(tile1) == type(tile2)
    # tile 1 is fixed in position...
    # tile 2 is mobile...
    col_to_match = tile1.sides()['c']
    base_options = list(tile2.sides().values())
    if col_to_match[::-1] in base_options:
        i = base_options.index(col_to_match[::-1])
        if i == 0: return None # matching col facing up
        i = rotate_nums(0, i)
        for _ in range(i):
            tile2.rotate()
        return None
    # now try flipping x
    tile2.flip_x()
    # tile2.flip_y()
    base_options = list(tile2.sides().values())
    if col_to_match[::-1] in base_options:
        i = base_options.index(col_to_match[::-1])
        if i == 0: return None # matching col facing left
        i = rotate_nums(0, i)
        for _ in range(i):
            tile2.rotate()
        return None
    raise AttributeError("Could not make tiles match up")

def refresh_tile_matches(tile_a: tile, matches: dict, all_sides: dict):
    tile_num = int(tile_a.name)
    # refresh side order in sides
    sides = tile_a.sides()
    all_sides[int(tile_num)] = sides
    letters = ['a','b','c','d']
    for let in letters:
        if let in matches[tile_num]:
            del matches[tile_num][let]
    for letter, side in all_sides[tile_num].items():
        for tile_num_2 in all_sides.keys():
                for letter_2, side_2 in all_sides[tile_num_2].items():
                    if tile_num == tile_num_2 and letter == letter_2:
                        continue
                    elif side == side_2[::-1] or side == side_2:
                        assert tile_num in matches
                        assert tile_num_2 in matches
                        matches[tile_num][letter]= {tile_num_2: letter_2}
                        matches[tile_num_2][letter_2]= {tile_num: letter}
    return matches, all_sides

def find_sea_monsters(image: list):
    sea_monster_image = [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   '
    ]
    sea_monster_search_locations = [(j, i) for j in range(3) for i in range(len(sea_monster_image[j])) if sea_monster_image[j].startswith('#', i)]
    monsters = []
    rows_to_go = len(image) - 2
    for row in range(rows_to_go):
        for column in range(len(image[0]) - 19):
            sub_image_slice = []
            sub_image_slice.append(image[row][column: (column + 21)])
            sub_image_slice.append(image[row + 1][column: (column + 21)])
            sub_image_slice.append(image[row + 2][column: (column + 21)])
            sea_monster_found_locations = [(j, i) for j in range(3) for i in range(len(sub_image_slice[j])) if sub_image_slice[j].startswith('#', i)]
            test = True
            for location in sea_monster_search_locations:
                if location not in sea_monster_found_locations:
                    test = False
                    break
            if test:
                print(f'Sea Monster Found: ({row},{column})')
                monsters.append((row, column))
    # now convert sea monsters to O

    for row, column in monsters:
        for j, i in sea_monster_search_locations:
            image[row + j] = image[row + j][:column + i] + 'O' + image[row + j][column + i + 1:] 

    return image




assert rotate_nums(1, 0) == 3

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
                    matches[tile_num_2][letter_2]= {tile_num: letter}
                    paired.add((tile_num_2, letter_2))
                    if 'match_counter' not in matches[tile_num]:
                        matches[tile_num]['match_counter'] = 0
                    matches[tile_num]['match_counter'] += 1
                    if 'match_counter' not in matches[tile_num_2]:
                        matches[tile_num_2]['match_counter'] = 0
                    matches[tile_num_2]['match_counter'] += 1

# find corners, where matches = 2
corners = []
for tile_a in matches:
    if matches[tile_a]['match_counter'] == 2:
        corners.append(tile_a)

# find edges, where matches = 3
edges = []
for tile_a in matches:
    if matches[tile_a]['match_counter'] == 3:
        edges.append(tile_a)

assert 4 == len(corners)
count_edges = len(edges)

# find middles, where matches = 4
middles = []
for tile_a in matches:
    if matches[tile_a]['match_counter'] == 4:
        middles.append(tile_a)

count_middles = len(middles)

# Build tile ID list
id_list = []
first_row = []
location_list = []

target_tile = corners[0]
location_list.append(find_tile_by_name(target_tile, tiles))
obj_1 = tiles[location_list[0]]
obj_1.flip_x()
matches, all_sides = refresh_tile_matches(obj_1, matches, all_sides)
first_row.append(target_tile)
if 'a' in matches[target_tile] and 'b' in matches[target_tile]:
    obj_1.rotate()
    obj_1.rotate()
elif 'b' in matches[target_tile] and 'c' in matches[target_tile]:
    obj_1.rotate()
    obj_1.rotate()
    obj_1.rotate()
elif 'd' in matches[target_tile] and 'a' in matches[target_tile]:
    obj_1.rotate()
matches, all_sides = refresh_tile_matches(obj_1, matches, all_sides)
target_tile = matches[target_tile]['d']

# Now corner piece is oriented properly

# iterate through item by item in the row until first row reaches second corner
# for remaining rows, 
end_row = False
while not end_row:
    target = int(list(target_tile.keys())[0])
    location_list.append(find_tile_by_name(target, tiles))
    obj_2 = tiles[location_list[-1]]
    first_row.append(target)
    align_right(obj_1, obj_2)
    matches, all_sides = refresh_tile_matches(obj_2, matches, all_sides)
    obj_1 = obj_2
    if matches[target]['match_counter'] == 2:
        end_row = True
    else:
        target_tile = matches[target]['d']
print()

id_list.append(first_row)
row_length = len(first_row)
row = first_row[:]

while len(id_list) < len(tiles) / row_length:
    end_row = False
    while not end_row:
        # Do first item in row
        target = row[0]
        target_tile = matches[target]['c']
        obj_1 = tiles[location_list[len(location_list)-row_length]]
        row.clear()
        target = int(list(target_tile.keys())[0])
        location_list.append(find_tile_by_name(target, tiles))
        obj_2 = tiles[location_list[-1]]
        row.append(target)
        align_down(obj_1, obj_2)
        matches, all_sides = refresh_tile_matches(obj_2, matches, all_sides)
        obj_1 = obj_2
        target_tile = matches[target]['d']
        for _ in  range(row_length - 1):
            target = int(list(target_tile.keys())[0])
            location_list.append(find_tile_by_name(target, tiles))
            obj_2 = tiles[location_list[-1]]
            row.append(target)
            align_right(obj_1, obj_2)
            matches, all_sides = refresh_tile_matches(obj_2, matches, all_sides)
            obj_1 = obj_2
            if matches[target]['match_counter'] < 4:
                end_row = True
            try:
                target_tile = matches[target]['d']
            except KeyError:
                pass
        id_list.append(copy.deepcopy(row))

print(id_list)

stripped_images = []
i = 0
for line in id_list:
    for a_tile in line:
        the_tile = tiles[location_list[i]]
        stripped_images.append(the_tile.strip_borders())
        i += 1

compiled_image = []
for tile_order in range(0, row_length):
    for row in range(8):
        write_row = ''
        for tile_iter in range(tile_order * row_length, row_length * (1 + tile_order)):
            write_row += stripped_images[tile_iter][row]
        compiled_image.append(copy.deepcopy(write_row))

compiled_tile = tile(compiled_image, 0)
print(compiled_tile)

# sea_monster_image = [
#     '                  # ',
#     '#    ##    ##    ###',
#     ' #  #  #  #  #  #   '
#     ]

for _ in range(4):
    compiled_tile.image = find_sea_monsters(compiled_tile.image)
    compiled_tile.rotate()
compiled_tile.flip_x()
for _ in range(4):
    compiled_tile.image = find_sea_monsters(compiled_tile.image)
    compiled_tile.rotate()
compiled_tile.flip_y()
for _ in range(4):
    compiled_tile.image = find_sea_monsters(compiled_tile.image)
    compiled_tile.rotate()

non_monsters = 0
for row in compiled_tile.image:
    non_monsters += row.count('#')
print('Part 2 Answer: ', non_monsters)
print(compiled_tile.image)

"""

'                  # '
'#    ##    ##    ###'
' #  #  #  #  #  #   '

"""