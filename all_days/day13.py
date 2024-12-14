# Day 13: Claw Contraption

# First star: The claw machines here are a little unusual. Instead of a joystick or directional buttons to control the
# claw, these machines have two buttons labeled A and B. Worse, you can't just put in a token and play; it costs 3
# tokens to push the A button and 1 token to push the B button.
# With a little experimentation, you figure out that each machine's buttons are configured to move the claw a specific
# amount to the right (along the X axis) and a specific amount forward (along the Y axis) each time that button is
# pressed.
# Each machine contains one prize; to win the prize, the claw must be positioned exactly above the prize on both the X
# and Y axes.
# You wonder: what is the smallest number of tokens you would have to spend to win as many prizes as possible? You
# assemble a list of every machine's button behavior and prize location (your puzzle input).
# You estimate that each button would need to be pressed no more than 100 times to win a prize. How else would someone
# be expected to play?
# Figure out how to win as many prizes as possible. What is the fewest tokens you would have to spend to win all
# possible prizes?

# Second star: As you go to win the first prize, you discover that the claw is nowhere near where you expected it would
# be. Due to a unit conversion error in your measurements, the position of every prize is actually 10000000000000 higher
# on both the X and Y axis!
# Add 10000000000000 to the X and Y position of every prize.
# Now, it is only possible to win a prize on the second and fourth claw machines. Unfortunately, it will take many more
# than 100 presses to do so.
# Using the corrected prize coordinates, figure out how to win as many prizes as possible. What is the fewest tokens you
# would have to spend to win all possible prizes?

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data


def parse_arcade(arcade):
    rules = {'A': {}, 'B': {}, 'prize': {}}
    order = ['A', 'B', 'prize']
    for i in range(3):
        x = arcade[i].find('X')
        y = arcade[i].find('Y')
        s = arcade[i].find(',')
        rules[order[i]]['X'] = int(arcade[i][(x + 2):s])
        rules[order[i]]['Y'] = int(arcade[i][(y + 2):])
    return rules


def play_all_arcades(data, fix = 0):
    tokens = 0
    for arcade in data:
        rules = parse_arcade(arcade)
        rules['prize']['X'] += fix
        rules['prize']['Y'] += fix
        parallel = rules['A']['X'] * rules['B']['Y'] - rules['A']['Y'] * rules['B']['X']
        if parallel == 0:
            print('----')
            print(arcade)
            print('----')
        else:
            A_coef = (rules['B']['Y'] * rules['prize']['X'] - rules['B']['X'] * rules['prize']['Y']) / parallel
            if (A_coef.is_integer()):
                B_coef = (rules['prize']['X'] - rules['A']['X'] * A_coef) / rules['B']['X']
                if (B_coef.is_integer()):
                    print('----')
                    print(arcade)
                    print([A_coef, B_coef])
                    print('----')
                    tokens += 3 * A_coef + B_coef
    return tokens


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day13.txt', by_block=True, numbers=False)

    if star == 1:  # The final answer is: 35997
        solution = play_all_arcades(data)
    elif star == 2:  # The final answer is: 82510994362072
        solution = play_all_arcades(data, 10000000000000)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
