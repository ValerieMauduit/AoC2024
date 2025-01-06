# Day 16: Reindeer Maze

# First star: The Reindeer start on the Start Tile (marked S) facing East and need to reach the End Tile (marked E).
# They can move forward one tile at a time (increasing their score by 1 point), but never into a wall (#). They can also
# rotate clockwise or counterclockwise 90 degrees at a time (increasing their score by 1000 points).
# Analyze your map carefully. What is the lowest score a Reindeer could possibly get?

# Second star: Every non-wall tile (S, ., or E) is equipped with places to sit along the edges of the tile. The most
# important factor to determine a good seat is whether the tile is on one of the best paths through the maze. If you sit
# somewhere else, you'd miss all the action!
# Analyze your map further. How many tiles are part of at least one of the best paths through the maze?

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data
from AoC_tools.work_with_maps import AocMap


def calculate_score_map(initial_map, initial_score=None, initial_position=None):
    reinder = initial_map
    if initial_score is None:
        initial_score = [0, 'H']
    if initial_position is None:
        initial_position = [1, reinder.height - 2]

    start = initial_position
    reinder.set_point(start, initial_score)
    previous_neighbours = [start]
    while len(previous_neighbours) > 0:
        next_neighbours = []
        for n0 in previous_neighbours:
            reinder.set_position(n0)
            for n1 in reinder.get_neighbours_coordinates(diagonals=False):
                point_n1_before = reinder.get_point(n1)
                if point_n1_before != '#':
                    n0_value = reinder.get_point(n0)
                    if n0[0] != n1[0]:
                        n1_value = [n0_value[0] + 1, 'H']
                    else:
                        n1_value = [n0_value[0] + 1, 'V']
                    if n1_value[1] != n0_value[1]:
                        n1_value[0] += 1000
                    if point_n1_before in ['.', 'E', 'S']:
                        reinder.set_point(n1, n1_value)
                        next_neighbours += [n1]
                    elif point_n1_before[0] > n1_value[0]:
                        reinder.set_point(n1, n1_value)
                        next_neighbours += [n1]
        previous_neighbours = next_neighbours
    return reinder


def get_one_best_path(score_map):
    best_seats = AocMap.empty_from_size(score_map.width, score_map.height)
    walls = score_map.get_marker_coords('#')
    best_seats.set_points(walls, '#')

    end = [score_map.width - 2, 1]
    previous_neighbours = [end]
    while len(previous_neighbours) > 0:
        next_neighbours = []
        for n0 in previous_neighbours:
            score_map.set_position(n0)
            local_score = score_map.get_point(n0)[0]
            best_seats.set_point(n0, 'O')
            for n1 in score_map.get_neighbours_coordinates(diagonals=False):
                if (best_seats.get_point(n1) not in ['#', 'O']) & (local_score != 'O'):
                    if local_score - score_map.get_point(n1)[0] in [1, 1001]:
                        next_neighbours += [n1]
        previous_neighbours = next_neighbours
    return best_seats.get_marker_coords('O')


def get_spots(data):
    best_seats_map = AocMap(data)
    reinder = calculate_score_map(AocMap(data))
    best_score = reinder.get_point([reinder.width - 2, 1])[0]
    best_seats_list = get_one_best_path(reinder)
    best_seats_map.set_points(best_seats_list, 'O')

    # Then check the neighbours of the best path to see if they could be in a best path
    neighbourhood = [
        pos
        for pos in best_seats_map.get_neighbourhood_coordinates(best_seats_list, diagonals=False)
        if best_seats_map.get_point(pos) not in ['S', 'E', '#', 'O']
    ]
    while len(neighbourhood) > 0:
        for pos in neighbourhood:
            new_score_map = calculate_score_map(AocMap(data), initial_position=pos, initial_score=reinder.get_point(pos))
            if new_score_map.get_point([reinder.width - 2, 1])[0] <= best_score:
                best_seats_list = get_one_best_path(new_score_map)
                if pos not in best_seats_list:
                    best_seats_list += [pos]
                best_seats_map.set_points(best_seats_list, 'O')
            else:
                best_seats_map.set_point(pos, '#')
        best_seats_list = best_seats_map.get_marker_coords('O')
        neighbourhood = [
            pos
            for pos in best_seats_map.get_neighbourhood_coordinates(best_seats_list, diagonals=False)
            if best_seats_map.get_point(pos) not in ['S', 'E', '#', 'O']
        ]

    # Summarize the result
    return len(best_seats_map.get_marker_coords('O'))


def reinder_score(data):
    reinder = calculate_score_map(data)
    return reinder.get_point([reinder.width - 2, 1])[0]


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day16.txt', numbers=False)

    if star == 1:  # The final answer is: 102488
        solution = reinder_score(AocMap(data))
    elif star == 2:  # The final answer is: 559
        solution = get_spots(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
