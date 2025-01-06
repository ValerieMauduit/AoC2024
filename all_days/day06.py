# Day 06: Guard Gallivant

# First star: You start by making a map (your puzzle input) of the situation.
# The map shows the current position of the guard with ^ (to indicate the guard is currently facing up from the
# perspective of the map). Any obstructions - crates, desks, alchemical reactors, etc. - are shown as #.
# Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following these steps:
# - If there is something directly in front of you, turn right 90 degrees.
# - Otherwise, take a step forward.
# Predict the path of the guard. How many distinct positions will the guard visit before leaving the mapped area?

# Second star: You need to get the guard stuck in a loop by adding a single new obstruction. How many different
# positions could you choose for this obstruction?

import os
import sys
import re
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data
from AoC_tools.work_with_maps import AocMap


def count_guard_displacement(data):
    next_direction = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
    y = [bool(re.search('\^', line)) for line in data].index(True)
    x = data[y].index('^')
    lab_map = AocMap(data, position=[x, y])
    direction = 'W'
    already_passed_here = 0
    too_many_superpositions = max([lab_map.width, lab_map.height])
    while (lab_map.get_neighbour(direction) != 'Exit') & (already_passed_here <= too_many_superpositions) :
        direction = next_direction[direction]
        while lab_map.get_neighbour(direction) not in ['#', 'Exit']:
            if lab_map.get_point(lab_map.get_position()) == 'X':
                already_passed_here += 1
            else:
                already_passed_here = 0
            lab_map.set_point(position=lab_map.get_position(), marker='X')
            lab_map.one_move(direction)
    if already_passed_here >= too_many_superpositions:
        return 'Loop'
    return lab_map.count_marker('X') + 1


def count_new_obstructions(data):
    counter = 0
    print(f"columns: {len(data[0])}")
    print(f"lines: {len(data)}")
    for x in range(len(data[0])):
        print(f"column {x}")
        for y in range(len(data)):
            new_lab_data = data.copy()
            if new_lab_data[y][x] != '^':
                new_lab_data[y] = new_lab_data[y][:x] + '#' + new_lab_data[y][(x + 1):]
                if count_guard_displacement(new_lab_data) == 'Loop':
                    counter += 1
        print(f"--- {counter} ---")
    return counter


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day06.txt', numbers=False)

    if star == 1:  # The final answer is: 4964
        solution = count_guard_displacement(data)
    elif star == 2:  # The final answer is: 1740
        solution = count_new_obstructions(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
