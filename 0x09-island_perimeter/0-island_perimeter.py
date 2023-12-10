#!/usr/bin/python3

def island_perimeter(grid):
    horizontal_length = []
    v_index = 0
    vertical_length = 0

    for line in grid:
        if check_island(line, 0, horizontal_length) is not None:
            horizontal = check_island(line, 0, horizontal_length)
            horizontal_length.append(horizontal['h_length'])
            if v_index != horizontal['starting_index']:
                v_index = horizontal['starting_index']
                vertical_length = 1
            else:
                vertical_length = vertical_length + 1
    return 2 * (vertical_length + max(horizontal_length))


def check_island(line, cur_index, h_length):
    if 1 in line:
        index = line.index(1, cur_index, len(line))
        new_h_length = 0
        h_length = count_island_length(line[index:])
        if 1 in line[h_length + index - 1:]:
            new_index = line.index(1, h_length + index - 1, len(line))
            new_h_length = count_island_length(line[new_index:])

        if h_length > new_h_length:
            return {'h_length': h_length, 'starting_index': index}
        else:
            return {'h_length': new_h_length, 'starting_index': new_index}
    return None

def count_island_length(line):
    h_length = 0
    for island in line:
        if island == 1:
            h_length = h_length + 1
        else:
            break
    return h_length