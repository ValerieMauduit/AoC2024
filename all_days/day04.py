# Day0: Ceres Search

# First star: As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like
# to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.
# This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other
# words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of
# them.
# Take a look at the little Elf's word search. How many times does XMAS appear?

# Second star: Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS
# puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X.
# How many times does an X-MAS appear?

import os
import sys
import re

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data
from AoC_tools.work_with_arrays import reverse_lines, vertical_lines, diagonals


def all_occurences(data):
    horizontal = data
    vertical = vertical_lines(data)
    diagonal_straight = diagonals(data)
    diagonal_back = diagonals(data, reverse=True)
    return sum([
        count_occurences(lines, 'XMAS') + count_occurences(lines, 'XMAS', back=True)
        for lines in [horizontal, vertical, diagonal_straight, diagonal_back]
    ])


def count_occurences(lines, pattern, back = False):
    if back:
        pattern = pattern[::-1]
    return sum([len(re.findall(pattern, ''.join(line))) for line in lines])


def count_crosses(data):
    n_rows = len(data)
    n_cols = len(data[0])
    return sum([is_x_mas([row[j:(j+3)] for row in data[i:(i+3)]]) for i in range(n_rows - 2) for j in range(n_cols - 2)])


def is_x_mas(square):
    if square[1][1] == 'A':
        corners = ''.join([square[0][0], square[0][2], square[2][2], square[2][0]])
        return corners in ['MMSS', 'SMMS', 'SSMM', 'MSSM']
    return False


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day04.txt', numbers=False)
    data = [[letter for letter in word] for word in data]

    if star == 1:  # The final answer is: 2447
        solution = all_occurences(data)
    elif star == 2:  # The final answer is: 1868
        solution = count_crosses(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
