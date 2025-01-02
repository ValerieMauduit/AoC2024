# Day05: Print Queue

# First star: Safety protocols clearly indicate that new pages for the safety manuals must be printed in a very specific
# order. The notation X|Y means that if both page number X and page number Y are to be produced as part of an update,
# page number X must be printed at some point before page number Y.
# The Elf has for you both the page ordering rules and the pages to produce in each update (your puzzle input), but
# can't figure out whether each update has the pages in the right order.
# For some reason, the Elves also need to know the middle page number of each update being printed. Because you are
# currently only printing the correctly-ordered updates, you will need to find the middle page number of each
# correctly-ordered update.
# Determine which updates are already in the correct order. What do you get if you add up the middle page number from
# those correctly-ordered updates?

# Second star: Find the updates which are not in the correct order. What do you get if you add up the middle page
# numbers after correctly ordering just those updates?

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data


def check_order(update, instructions):
    ordered = True
    index = 0
    n_instr = len(instructions) - 1
    while ordered & (index < n_instr):
        instr = instructions[index]
        index += 1
        if (instr[0] in update) & (instr[1] in update):
            ordered = update.index(instr[0]) < update.index(instr[1])
    return ordered


def sort_update(update, instructions):
    while not check_order(update, instructions):
        for instr in instructions:
            if (instr[0] in update) & (instr[1] in update):
                ind0, ind1 = update.index(instr[0]), update.index(instr[1])
                if ind0 > ind1 :
                    update = update[:ind1] + [instr[0]] + update[ind1:ind0] + update[ind0+1:]
    return update


def get_middle(update):
    return update[int((len(update) - 1)/ 2)]


def result(updates, instructions):
    return sum([get_middle(update) for update in updates if check_order(update, instructions)])


def sorted_ones_result(updates, instructions):
    return sum([
        get_middle(sort_update(update, instructions)) for update in updates if not check_order(update, instructions)
    ])


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day05.txt', numbers=False, by_block=True)
    instructions = [[int(number) for number in pair.split('|')] for pair in data[0]]
    updates = [[int(page) for page in update.split(',')] for update in data[1]]

    if star == 1:  # The final answer is: 6267
        solution = result(updates, instructions)
    elif star == 2:  # The final answer is: 5184
        solution = sorted_ones_result(updates, instructions)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
