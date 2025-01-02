# Day 25: Code Chronicle

# First star: The best they can do is send over schematics of every lock and every key for the floor you're on (your
# puzzle input).
# The locks are schematics that have the top row filled (#) and the bottom row empty (.); the keys have the top row
# empty and the bottom row filled. If you look closely, you'll see that each schematic is actually a set of columns of
# various heights, either extending downward from the top (for locks) or upward from the bottom (for keys).
# For locks, those are the pins themselves; you can convert the pins in schematics to a list of heights, one per column.
# For keys, the columns make up the shape of the key where it aligns with pins; those can also be converted to a list of
# heights.
# These seem like they should fit together; in the first four columns, the pins and key don't overlap. However, this key
# cannot be for this lock: in the rightmost column, the lock's pin overlaps with the key, which you know because in that
# column the sum of the lock height and key height is more than the available space.
# Analyze your lock and key schematics. How many unique lock/key pairs fit together without overlapping in any column?

# Second star: description

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data
from AoC_tools.work_with_lists import count_value, transpose


def doors_and_keys(data):
    doors, keys = [], []
    for block in data:
        transposed = transpose(block)
        columns = [count_value('#', in_list=row) for row in transposed]
        if all([character == '#' for character in block[0]]):
            doors += [columns]
        else:
            keys += [columns]
    return {'doors': doors, 'keys': keys}


def fitting_doors_and_keys(data):
    all_counts = doors_and_keys(data)
    count = 0
    for door in all_counts['doors']:
        for key in all_counts['keys']:
            count += max([x + y for x, y in zip(door, key)]) <= 7
    return count


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day25.txt', numbers=False, by_block=True)

    if star == 1:  # The final answer is: 3021
        solution = fitting_doors_and_keys(data)
    elif star == 2:  # The final answer is:
        solution = my_func(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
