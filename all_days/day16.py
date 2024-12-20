# Day 16: Reindeer Maze

# First star: The Reindeer start on the Start Tile (marked S) facing East and need to reach the End Tile (marked E).
# They can move forward one tile at a time (increasing their score by 1 point), but never into a wall (#). They can also
# rotate clockwise or counterclockwise 90 degrees at a time (increasing their score by 1000 points).
#Analyze your map carefully. What is the lowest score a Reindeer could possibly get?

# Second star: description

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data
from AoC_tools.work_with_maps import AocMap


def move_to_exit(maze, direction='E', score=0):
    if maze.get_position() == [maze.width - 2, 1]:
        return score
    if '.' in maze.get_neighbours(diagonals=False):
        neighbour_scores = []
        for d in ['N', 'S', 'E', 'W']:
            if maze.get_neighbour(d) == '.':
                maze.set_point(maze.get_position(), 'X')
                maze.one_move(d)
                neighbour_scores += [score + 1 + 1000 * int(d != direction) + move_to_exit(maze, d, score)]
        return min(neighbour_scores)


def reinder_score(data):
    reinder = AocMap(data)
    reinder.set_position([1, reinder.height - 2])
    return move_to_exit(reinder)


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day16.txt', numbers=False)

    if star == 1:  # The final answer is:
        solution = my_func(data)
    elif star == 2:  # The final answer is:
        solution = my_func(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
