# Day 18: RAM Run

# First star: The algorithm is fast - it's going to cause a byte to fall into your memory space once every nanosecond!
# Fortunately, you're faster, and by quickly scanning the algorithm, you create a list of which bytes will fall (your
# puzzle input) in the order they'll land in your memory space.
# Your memory space is a two-dimensional grid with coordinates that range from 0 to 70 both horizontally and vertically.
# Each byte position is given as an X,Y coordinate, where X is the distance from the left edge of your memory space and
# Y is the distance from the top edge of your memory space.
# You and The Historians are currently in the top left corner of the memory space (at 0,0) and need to reach the exit in
# the bottom right corner. You'll need to simulate the falling bytes to plan out where it will be safe to run; for now,
# simulate just the first few bytes falling into your memory space.
# As bytes fall into your memory space, they make that coordinate corrupted. Corrupted memory coordinates cannot be
# entered by you or The Historians, so you'll need to plan your route carefully. You also cannot leave the boundaries of
# the memory space; your only hope is to reach the exit.
# You can take steps up, down, left, or right.
# Simulate the first kilobyte (1024 bytes) falling onto your memory space. Afterward, what is the minimum number of
# steps needed to reach the exit?

# Second star: To determine how fast everyone needs to go, you need to determine the first byte that will cut off the
# path to the exit.
# Simulate more of the bytes that are about to corrupt your memory space. What are the coordinates of the first byte
# that will prevent the exit from being reachable from your starting position? (Provide the answer as two integers
# separated by a comma with no other characters.)

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data
from AoC_tools.work_with_maps import AocMap


def exit_map(data, size=70, corrupted=1024):
    memory = AocMap.from_coord(data[:corrupted], x_min=0, y_min=0, x_max=size, y_max=size)
    first_point = [0, 0]
    value = 0
    memory.set_point(first_point, value)
    previous_points = [first_point]
    while len(previous_points) > 0:
        next_points = []
        value += 1
        for n0 in previous_points:
            memory.set_position(n0)
            for n1 in memory.get_neighbours_coordinates(diagonals=False):
                if memory.get_point(n1) == '.':
                    next_points += [n1]
                    memory.set_point(n1, value)
        previous_points = next_points
    return memory.get_point([memory.width - 1, memory.height - 1])


def get_last_corruption(data, size=70):
    min_corrupt = 1024
    max_corrupt = len(data) - 1
    while min_corrupt < max_corrupt - 1:
        corrupt = int(0.5 * (min_corrupt + max_corrupt))
        new_value = exit_map(data, size, corrupt)
        if new_value == '.':
            max_corrupt = corrupt
        else:
            min_corrupt = corrupt
    return data[min_corrupt]


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day18.txt', split=',')

    if star == 1:  # The final answer is: 382
        solution = exit_map(data)
    elif star == 2:  # The final answer is: 6,36
        solution = get_last_corruption(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
