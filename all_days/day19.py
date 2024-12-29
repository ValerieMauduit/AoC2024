# Day 19: Linen Layout

# First star: Every towel at this onsen is marked with a pattern of colored stripes. There are only a few patterns, but
# for any particular pattern, the staff can get you as many towels with that pattern as you need. Each stripe can be
# white (w), blue (u), black (b), red (r), or green (g).
# The Official Onsen Branding Expert has produced a list of designs - each a long sequence of stripe colors - that they
# would like to be able to display. You can use any towels you want, but all of the towels' stripes must exactly match
# the desired design.
# To start, collect together all of the available towel patterns and the list of desired designs (your puzzle input).
# To get into the onsen as soon as possible, consult your list of towel patterns and desired designs carefully. How many
# designs are possible?

# Second star: The staff don't really like some of the towel arrangements you came up with. To avoid an endless cycle of
# towel rearrangement, maybe you should just give them every possible option.
# They'll let you into the onsen as soon as you have the list. What do you get if you add up the number of different
# ways you could make each design?

import os
import sys
import re

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data
from AoC_tools.work_with_dicts import update_dict


def indispensable_towels(towels):
    list_of_indispensable = []
    for towel in towels:
        light_towels = [t for t in towels if t != towel]
        if not possible_pattern(towel, light_towels):
            list_of_indispensable += [towel]
    return list_of_indispensable


def possible_pattern(pattern, towels, lead=''):
    if pattern in towels:
        return True
    else:
        possible, n = False, 0
        possible_towels = [t for t in towels if t == pattern[:len(t)]]
        while (not possible) & (n < len(possible_towels)):
            towel = possible_towels[n]
            if possible_pattern(pattern[len(towel):], towels, lead + '  '):
                possible = True
            else:
                n += 1
        return possible


def count_possible_patterns(data):
    set_of_towels = indispensable_towels(data['towels'])
    count = 0
    for p in data['patterns']:
        possible = possible_pattern(p, set_of_towels)
        if possible:
            count += 1
    return count


def all_possibilities_for_a_pattern(pattern, towels):
    pattern_decompositions = [[pattern]]
    possibilities = []
    while len(pattern_decompositions) > 0:
        new_pattern_decompositions = []
        for decomposition in pattern_decompositions:
            for towel in towels:
                if decomposition[-1] == towel:
                    possibilities += [decomposition]
                elif decomposition[-1][:len(towel)] == towel:
                    new_pattern_decompositions += [decomposition[:-1] + [towel, decomposition[-1][len(towel):]]]
        pattern_decompositions = new_pattern_decompositions
    return possibilities


def recompose(splitted_pattern, towel):
    joined_towel = '-' + ''.join(towel.split('-')) + '-'
    count = len(splitted_pattern) - 1
    patterns = [splitted_pattern]
    for n in range(count):
        patterns = (
                [p[:(2 * n + 1)] + [towel] + p[(2 * n + 1):] for p in patterns]
                + [p[:(2 * n + 1)] + [joined_towel] + p[(2 * n + 1):] for p in patterns]
        )
    return [''.join(p) for p in patterns]


def count_splits(indexes, length):
    indexes = [i + [1] for i in indexes]
    count = 0
    while len(indexes) > 0:
        first_sets = [i for i in indexes if i[0] == 0]
        next_steps = []
        for first in first_sets:
            next_possibilities = [i for i in indexes if i[0] == first[1]]
            if len(next_possibilities) == 0:
                if first[1] == length:
                    count += first[2]
            else:
                next_steps += [[0, i[1], first[2]] for i in next_possibilities]
        if len(next_steps) > 0:
            second = set([i[1] for i in next_steps])
            next_steps = [[0, s, sum([i[2] for i in next_steps if i[1] == s])] for s in second]
            possible_next = [i for i in indexes if i[0] >= min([j[1] for j in next_steps])]
            if len(possible_next) > 0:
                indexes = next_steps + possible_next
            else:
                indexes = next_steps
        else:
            indexes = []
    return count


def count_all_possibilities_for_all_patterns(data):
    count = 0
    all_patterns = data['patterns']
    all_towels = data['towels']
    for pattern in all_patterns:
        print(pattern)
        pattern_dict = {}
        for towel in all_towels:
            if towel in pattern:
                indexes = []
                for i in range(len(pattern) - len(towel) + 1):
                    if pattern[i:(i + len(towel))] == towel:
                        indexes += [i]

                for index in indexes:
                    pattern_dict = update_dict(pattern_dict, index, len(towel), cumulative=False)
        indexes = list(pattern_dict.keys())
        indexes.sort()
        pattern_indexation = []
        for i in indexes:
            for v in pattern_dict[i]:
                pattern_indexation += [[i, i + v]]
        local_count = count_splits(pattern_indexation, len(pattern))
        print(f'    {local_count}')
        count += local_count
    return count


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day19.txt', numbers=False, by_block=True)
    data = {'towels': data[0][0].split(', '), 'patterns': data[1]}

    if star == 1:  # The final answer is: 287
        solution = count_possible_patterns(data)
    elif star == 2:  # The final answer is: 571894474468161
        solution = count_all_possibilities_for_all_patterns(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
