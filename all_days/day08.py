# Day 8: Resonant Collinearity

# First star: Scanning across the city, you find that there are actually many such antennas. Each antenna is tuned to a
# specific frequency indicated by a single lowercase letter, uppercase letter, or digit. You create a map (your puzzle
# input) of these antennas.
# The signal only applies its nefarious effect at specific antinodes based on the resonant frequencies of the antennas.
# In particular, an antinode occurs at any point that is perfectly in line with two antennas of the same frequency - but
# only when one of the antennas is twice as far away as the other. This means that for any pair of antennas with the
# same frequency, there are two antinodes, one on either side of them.
# However, antinodes can occur at locations that contain antennas.
# Calculate the impact of the signal. How many unique locations within the bounds of the map contain an antinode?
# Second star: description

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data


def get_antenna_positions(data, symbol):
    positions = []
    for line in range(len(data)):
        for col in range(len(data[0])):
            if data[line][col] == symbol:
                positions.append([col, line])
    return positions


def get_antinodes(antenna_positions):
    positions = []
    nb_antenna = len(antenna_positions)
    for i in range(nb_antenna - 1):
        antenna1 = antenna_positions[i]
        for j in range(i + 1, nb_antenna):
            antenna2 = antenna_positions[j]
            positions.append([2 * antenna1[0] - antenna2[0], 2 * antenna1[1] - antenna2[1]])
            positions.append([2 * antenna2[0] - antenna1[0], 2 * antenna2[1] - antenna1[1]])
    return positions


def get_all_antinodes(data):
    antinodes = []
    for symbol in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        antennas = get_antenna_positions(data, symbol)
        antinodes += get_antinodes(antennas)
        height, width = len(data), len(data[0])
    return [
        antinode for antinode in antinodes
        if (antinode[0] >= 0) & (antinode[0] <= width) & (antinode[1] >= 0) & (antinode[1] <= height)
    ]


def count_all_antinodes(data):
    return len(set([x[0] * 10000 + x[1] for x in get_all_antinodes(data)]))


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day08.txt', numbers=False)
    data = [[x for x in line] for line in data]

    if star == 1:  # The final answer is:
        solution = count_all_antinodes(data)
    elif star == 2:  # The final answer is:
        solution = my_func(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
