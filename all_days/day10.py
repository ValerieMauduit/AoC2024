# Day 10: Hoof It

# First star: The topographic map indicates the height at each position using a scale from 0 (lowest) to 9 (highest).
# Based on un-scorched scraps of the book, you determine that a good hiking trail is as long as possible and has an
# even, gradual, uphill slope. For all practical purposes, this means that a hiking trail is any path that starts at
# height 0, ends at height 9, and always increases by a height of exactly 1 at each step. Hiking trails never include
# diagonal steps - only up, down, left, or right (from the perspective of the map).
# A trailhead is any position that starts one or more hiking trails - here, these positions will always have height 0.
# Assembling more fragments of pages, you establish that a trailhead's score is the number of 9-height positions
# reachable from that trailhead via a hiking trail.
# The reindeer gleefully carries over a protractor and adds it to the pile. What is the sum of the scores of all
# trailheads on your topographic map?

# Second star: A trailhead's rating is the number of distinct hiking trails which begin at that trailhead.
# What is the sum of the ratings of all trailheads?

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data
from AoC_tools.work_with_maps import AocMap


def count_paths(topographic_map, with_variants=False):
    count = 0
    for y in range(topographic_map.height):
        for x in range(topographic_map.width):
            if topographic_map.get_point([x, y]) == 0:
                if with_variants:
                    count += get_point_score([x, y], topographic_map)
                else:
                    count += len(get_point_nines([x, y], topographic_map))
    return count


def get_point_nines(point, topographic_map, nines=None, value=0):
    if nines is None:
        nines = []
    if value == 9:
        nines += [f'{point[0]} - {point[1]}']
        return list(set(nines))
    topographic_map.set_position(point)
    for neighbour in topographic_map.get_neighbours_coordinates(diagonals=False):
        if topographic_map.get_point(neighbour) == value + 1:
            nines += get_point_nines(neighbour, topographic_map, nines, value=value + 1)
    return list(set(nines))


def get_point_score(point, topographic_map, value=0):
    if value == 9:
        return 1
    topographic_map.set_position(point)
    if (value + 1) not in topographic_map.get_neighbours(diagonals=False):
        return 0
    return sum([
        get_point_score(neighbour, topographic_map, value=value + 1)
        for neighbour in topographic_map.get_neighbours_coordinates(diagonals=False)
        if topographic_map.get_point(neighbour) == value + 1
    ])


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day10.txt', numbers=False)
    topographic_map = AocMap(data, numbers=True)

    if star == 1:  # The final answer is: 629
        solution = count_paths(topographic_map)
    elif star == 2:  # The final answer is: 1242
        solution = count_paths(topographic_map, with_variants=True)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
