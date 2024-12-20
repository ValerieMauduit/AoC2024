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
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data


def indispensable_towels(towels):
    list_of_indispensable = []
    for towel in towels:
        light_towels = [t for t in towels if t != towel]
        if not possible_pattern(towel, light_towels):
            list_of_indispensable += [towel]
    return list_of_indispensable


def possible_pattern(pattern, towels, lead = ''):
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


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day19.txt', numbers=False, by_block=True)
    data = {'towels': data[0][0].split(', '), 'patterns': data[1]}

    if star == 1:  # The final answer is: 287
        solution = count_possible_patterns(data)
    elif star == 2:  # The final answer is:
        solution = my_func(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
