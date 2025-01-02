# Day 20: Race Condition

# First star: The race takes place on a particularly long and twisting code path; programs compete to see who can finish
# in the fewest picoseconds. The winner even gets their very own mutex!
# They hand you a map of the racetrack (your puzzle input).
# The map consists of track (.) - including the start (S) and end (E) positions (both of which also count as track) -
# and walls (#).
# When a program runs through the racetrack, it starts at the start position. Then, it is allowed to move up, down,
# left, or right; each such move takes 1 picosecond. The goal is to reach the end position as quickly as possible.
# Because there is only a single path from the start to the end and the programs all go the same speed, the races used
# to be pretty boring. To make things more interesting, they introduced a new rule to the races: programs are allowed to
# cheat.
# The rules for cheating are very strict. Exactly once during a race, a program may disable collision for up to 2
# picoseconds. This allows the program to pass through walls as if they were regular track. At the end of the cheat, the
# program must be back on normal track again; otherwise, it will receive a segmentation fault and get disqualified.
# You aren't sure what the conditions of the racetrack will be like, so to give yourself as many options as possible,
# you'll need a list of the best cheats. How many cheats would save you at least 100 picoseconds?


# Second star: The programs seem perplexed by your list of cheats. Apparently, the two-picosecond cheating rule was
# deprecated several milliseconds ago! The latest version of the cheating rule permits a single cheat that instead lasts
# at most 20 picoseconds.
# Cheats don't need to use all 20 picoseconds; cheats can last any amount of time up to and including 20 picoseconds
# (but can still only end when the program is on normal track). Any cheat time not used is lost; it can't be saved for
# another cheat later.
# Find the best cheats using the updated cheating rules. How many cheats would save you at least 100 picoseconds?

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data
from AoC_tools.work_with_maps import AocMap
from AoC_tools.work_with_dicts import update_dict


def original_track(race_map):
    start_point = race_map.get_marker_coords('S')[0]
    race_map.set_position(start_point)
    full_path = []
    next_point = [n for n in race_map.get_neighbours_coordinates(diagonals=False) if race_map.get_point(n) == '.']
    while len(next_point) > 0:
        full_path += [race_map.get_position()]
        race_map.set_point(race_map.get_position(), '*')
        race_map.set_position(next_point[0])
        next_point = [n for n in race_map.get_neighbours_coordinates(diagonals=False) if race_map.get_point(n) == '.']
    full_path += [race_map.get_position()]
    next_point = [n for n in race_map.get_neighbours_coordinates(diagonals=False) if race_map.get_point(n) == 'E']
    full_path += [next_point[0]]
    return full_path


def get_all_cheats(race_path):
    cheat_count = {}
    base = 1000
    race_coords = [base * x[0] + x[1] for x in race_path]
    for pos in range(1, len(race_coords)):
        for value in [race_coords[pos] - 2 * base, race_coords[pos] + 2 * base, race_coords[pos] - 2, race_coords[pos] + 2]:
            if value in race_coords[:(pos - 1)]:
                diff = pos - race_coords.index(value) - 2
                if (diff > 0) & (diff in cheat_count.keys()):
                    cheat_count[diff] += 1
                elif diff > 0:
                    cheat_count[diff] = 1
    return cheat_count


def count_cheats(race_map, minimum_cheat=100):
    race_track = original_track(race_map)
    all_cheats = get_all_cheats(race_track)
    return sum([v for k, v in all_cheats.items() if k >= minimum_cheat])


def get_advanced_cheats(race_path, max_length=20):
    cheat_count = {}
    for pos in range(1, len(race_path)):
        if pos % 1000 == 0:
            print(f'   x = {pos}')
        for prev in range(0, pos - 1):
            cheat_distance = abs(race_path[pos][0] - race_path[prev][0]) + abs(race_path[pos][1] - race_path[prev][1])
            if cheat_distance <= max_length:
                diff = pos - prev
                cheat_count = update_dict(cheat_count, diff - cheat_distance, 1, cumulative=True)
    return cheat_count


def count_advanced_cheats(race_map, minimum_cheat=100, max_length=20):
    race_track = original_track(race_map)
    print(f'race path done, length = {len(race_track)}')
    all_cheats = get_advanced_cheats(race_track, max_length)
    print('all cheats done')
    return sum([v for k, v in all_cheats.items() if k >= minimum_cheat])


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day20.txt', numbers=False)
    race_map = AocMap(data)

    if star == 1:  # The final answer is: 1393
        solution = count_cheats(race_map)
    elif star == 2:  # The final answer is: 990096
        solution = count_advanced_cheats(race_map)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
