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


def reinder_map(data, initial_score=None):
    if initial_score is None:
        initial_score = [0, 'H']
    reinder = AocMap(data)
    start = [1, reinder.height - 2]
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
                    if point_n1_before in ['.', 'E']:
                        reinder.set_point(n1, n1_value)
                        next_neighbours += [n1]
                    elif point_n1_before[0] > n1_value[0]:
                        reinder.set_point(n1, n1_value)
                        next_neighbours += [n1]
        previous_neighbours = next_neighbours
    return reinder


def calculate_good_seat(point, score_map, best_seats):
    good_seat = False
    previous_neighbours = [point]
    new_map = AocMap.empty_from_size(score_map.width, score_map.height)
    new_map.set_point(point, score_map.get_point(point))
    new_map.set_points(score_map.get_marker_coords('#'), '#')
    new_map.set_point(point, score_map.get_point(point))
    while (not good_seat) & (len(previous_neighbours) > 0):
        next_neighbours = []
        for n0 in previous_neighbours:
            new_map.set_position(n0)
            n0_value = new_map.get_point(n0)
            input(f'Parent {n0}, value {n0_value}')
            print(new_map.get_neighbours_coordinates(diagonals=False))
            for n1 in new_map.get_neighbours_coordinates(diagonals=False):
                point_n1_before = new_map.get_point(n1)
                print(f'   neighbour {n1}, value {point_n1_before}')
                if point_n1_before != '#':
                    # Set + 1 translation
                    if n0[0] != n1[0]:
                        n1_value = [n0_value[0] + 1, 'H']
                    else:
                        n1_value = [n0_value[0] + 1, 'V']
                    # Set rotation score
                    if n1_value[1] != n0_value[1]:
                        n1_value[0] += 1000
                    print(f'   neighbour {n1}, new value {n1_value}')
                    # Check if arrived of good seat
                    if best_seats.get_point(n1) == 'O':
                        print('        back on seat')
                        print(f'        value in score map {score_map.get_point(n1)}')
                        if n1_value[0] <= score_map.get_point(n1)[0]:
                            print('good seat!')
                            good_seat = True
                    # Or continue digging in the submap
                    else:
                        if point_n1_before in ['.', 'E']:
                            print('      score is set')
                            new_map.set_point(n1, n1_value)
                            next_neighbours += [n1]
                        elif point_n1_before[0] > n1_value[0]:
                            print('      score is updated')
                            new_map.set_point(n1, n1_value)
                            next_neighbours += [n1]
            previous_neighbours = next_neighbours
    return good_seat


def get_spots(data):
    reinder = reinder_map(data)
    best_seats = AocMap.empty_from_size(reinder.width, reinder.height)
    walls = reinder.get_marker_coords('#')
    best_seats.set_points(walls, '#')

    # First get the obvious best path
    end = [reinder.width - 2, 1]
    previous_neighbours = [end]
    while len(previous_neighbours) > 0:
        next_neighbours = []
        for n0 in previous_neighbours:
            reinder.set_position(n0)
            local_score = reinder.get_point(n0)[0]
            best_seats.set_point(n0, 'O')
            for n1 in reinder.get_neighbours_coordinates(diagonals=False):
                if (best_seats.get_point(n1) not in ['#', 'O']) & (local_score != 'O'):
                    if local_score - reinder.get_point(n1)[0] in [1, 1001]:
                        next_neighbours += [n1]
        previous_neighbours = next_neighbours
    best_seats.display()
    input('...')

    # Then check the neighbours of the best path to see if they could be in a best path
    neighbourhood = [
        p
        for p in best_seats.get_neighbourhood_coordinates(best_seats.get_marker_coords('O'), diagonals=False)
        if reinder.get_point(p) not in ['S', 'E', '#']
    ]
    neighbourhood = [[1, 10]]
    while len(neighbourhood) > 0:
        print(f'Neighbours: {neighbourhood}')
        kept_points = []
        for n0 in neighbourhood:
            if calculate_good_seat(n0, reinder, best_seats):
                best_seats.set_point(n0, 'O')
                kept_points += [n0]
            else:
                best_seats.set_point(n0, '#')
                reinder.set_point(n0, '#')
        neighbourhood = [
            p
            for p in reinder.get_neighbourhood_coordinates(kept_points, diagonals=False)
            if reinder.get_point(p) not in ['S', 'E', '#']
        ]
        print(f'Kept points: {kept_points}')
        best_seats.display()
        input('...')

    # Summarize the result
    return len(best_seats.get_marker_coords('O'))


def reinder_score(data):
    reinder = reinder_map(data)
    return reinder.get_point([reinder.width - 2, 1])[0]


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day16.txt', numbers=False)

    if star == 1:  # The final answer is: 102488
        solution = reinder_score(data)
    elif star == 2:  # The final answer is:
        solution = get_spots(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
