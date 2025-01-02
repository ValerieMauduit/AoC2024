# Day 15: Warehouse Woes

# First star: The lanternfish already have a map of the warehouse and a list of movements the robot will attempt to make
# (your puzzle input). The problem is that the movements will sometimes fail as boxes are shifted around, making the
# actual movements of the robot difficult to predict.
# As the robot (@) attempts to move, if there are any boxes (O) in the way, the robot will also attempt to push those
# boxes. However, if this action would cause the robot or a box to move into a wall (#), nothing moves instead,
# including the robot. The initial positions of these are shown on the map at the top of the document the lanternfish
# gave you.
# The rest of the document describes the moves (^ for up, v for down, < for left, > for right) that the robot will
# attempt to make, in order. (The moves form a single giant sequence; they are broken into multiple lines just to make
# copy-pasting easier. Newlines within the move sequence should be ignored.)
# The lanternfish use their own custom Goods Positioning System (GPS for short) to track the locations of the boxes. The
# GPS coordinate of a box is equal to 100 times its distance from the top edge of the map plus its distance from the
# left edge of the map. (This process does not stop at wall tiles; measure all the way to the edges of the map.)
# Predict the motion of the robot and boxes in the warehouse. After the robot is finished moving, what is the sum of all
# boxes' GPS coordinates?

# Second star: This warehouse's layout is surprisingly similar to the one you just helped. There is one key difference:
# everything except the robot is twice as wide! The robot's list of movements doesn't change.
# To get the wider warehouse's map, start with your original map and, for each tile, make the following changes:
# - If the tile is #, the new map contains ## instead.
# - If the tile is O, the new map contains LR instead.
# - If the tile is ., the new map contains .. instead.
# - If the tile is @, the new map contains @. instead.
# This will produce a new warehouse map which is twice as wide and with wide boxes that are represented by LR. (The
# robot does not change size.)
# This warehouse also uses GPS to locate the boxes. For these larger boxes, distances are measured from the edge of the
# map to the closest edge of the box in question.
# Predict the motion of the robot and boxes in this new, scaled-up warehouse. What is the sum of all boxes' final GPS
# coordinates?

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data
from AoC_tools.work_with_maps import AocMap


def move_robot(warehouse_map, move):
    line = warehouse_map.get_line(move)
    if '.' in line:
        first_place = line.index('.')
        if '#' not in line[:(first_place + 1)]:
            # Move the boxes
            line_positions = warehouse_map.get_line_positions(move)
            warehouse_map.set_points(line_positions[1:(first_place + 1)], line[:first_place])
            # Move the robot
            warehouse_map.set_point(warehouse_map.get_position(), '.')
            warehouse_map.one_move(move)
            warehouse_map.set_point(warehouse_map.get_position(), '@')
    return warehouse_map


def check_sum(data):
    warehouse, moves = data[0], ''.join(data[1])
    warehouse_map = AocMap(warehouse)
    # Robot initial position
    warehouse_map.set_position(warehouse_map.get_marker_coords('@')[0])
    # Make all the moves
    for move in moves:
        warehouse_map = move_robot(warehouse_map, move)
    # Checksum of the boxes
    boxes = warehouse_map.get_marker_coords('O')
    return sum([box[0] + 100 * box[1] for box in boxes])


def move_robot_vertical(warehouse_map, direction):
    moved, blocked = False, False
    positions = [[warehouse_map.get_position()]]
    sense = -1
    if direction == 'S':
        sense = 1
    while (not moved) & (not blocked):
        lower_block = [[pos[0], pos[-1] + sense] for pos in positions[-1]]
        values = warehouse_map.get_points(lower_block)
        if '#' in values:
            blocked = True
        elif ('L' in values) | ('R' in values):
            # Create next block
            lower_block += [[x[0] - 1, x[1]] for x in lower_block if warehouse_map.get_point(x) == 'R']
            lower_block += [[x[0] + 1, x[1]] for x in lower_block if warehouse_map.get_point(x) == 'L']
            lower_block = [x for x in lower_block if warehouse_map.get_point(x) != '.']
            positions += [lower_block]
        else:
            moved = True
            # Move
            pos_to_set = []
            markers = []
            for line in range(len(positions)):
                for pos in positions[line]:
                    pos_to_set += [[pos[0], pos[1] + sense]]
                    markers += [warehouse_map.get_point(pos)]
                    if line == 0:
                        pos_to_set += [pos]
                        markers += ['.']
                    elif [pos[0], pos[1] - sense] not in positions[line -1]:
                        pos_to_set += [pos]
                        markers += ['.']
            warehouse_map.set_points(pos_to_set, markers)
            warehouse_map.set_point(warehouse_map.get_position(), '.')
            warehouse_map.one_move(direction)
            warehouse_map.set_point(warehouse_map.get_position(), '@')
    return warehouse_map


def second_warehouse_checksum(data):
    warehouse = []
    for line in data[0]:
        new_line = ['.'] * len(line) * 2
        for n in range(len(line)):
            if line[n] == '#':
                new_line[(2 * n):(2 * n + 2)] = ['#', '#']
            elif line[n] == 'O':
                new_line[(2 * n):(2 * n + 2)] = ['L', 'R']
            elif line[n] == '@':
                new_line[(2 * n):(2 * n + 2)] = ['@', '.']
        warehouse += [new_line]
    moves = ''.join(data[1])
    warehouse_map = AocMap(warehouse)
    warehouse_map.display()
    # Robot initial position
    warehouse_map.set_position(warehouse_map.get_marker_coords('@')[0])
    # Make all the moves
    for move in moves:
        if move in ['W', 'E']:
            warehouse_map = move_robot(warehouse_map, move)
        else:
            warehouse_map = move_robot_vertical(warehouse_map, move)
    warehouse_map.display()
    # Checksum of the boxes
    boxes = warehouse_map.get_marker_coords('L')
    return sum([box[0] + 100 * box[1] for box in boxes])


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day15.txt', numbers=False, by_block=True)

    if star == 1:  # The final answer is: 1492518
        solution = check_sum(data)
    elif star == 2:  # The final answer is: 1512860
        solution = second_warehouse_checksum(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
