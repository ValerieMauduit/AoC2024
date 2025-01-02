# Day1: Historian Hysteria

# First star:
# Maybe the lists are only off by a small amount! To find out, pair up the numbers and measure how far apart they are.
# Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left
# number with the second-smallest right number, and so on.
# To find the total distance between the left list and the right list, add up the distances between all of the pairs you
# found.

# Second star:
# This time, you'll need to figure out exactly how often each number from the left list appears in the right list.
# Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of
# times that number appears in the right list.

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data


def sort(locations, column):
    ids = [id_pair[column] for id_pair in locations]
    ids.sort()
    return ids


def distance_sum(locations):
    left = sort(locations, 0)
    right = sort(locations, 1)
    return sum([abs(x - y) for x, y in zip(left, right)])


def comparisons(locations):
    left = sort(locations, 0)
    right = sort(locations, 1)
    return sum([x * right.count(x) for x in left])


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day01.txt', split='   ')
    if star == 1:  # The final answer is: 2164381
        solution = distance_sum(data)
    elif star == 2:  # The final answer is: 20719933
        solution = comparisons(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
