# Day 7: Bridge Repair

# First star: Each line represents a single equation. The test value appears before the colon on each line; it is your
# job to determine whether the remaining numbers can be combined with operators to produce the test value.
# Operators are always evaluated left-to-right, not according to precedence rules. Furthermore, numbers in the equations
# cannot be rearranged.
# The engineers just need the total calibration result, which is the sum of the test values from just the equations that
# could possibly be true.

# Second star: Just then, you spot your mistake: some well-hidden elephants are holding a third type of operator.
# The concatenation operator (||) combines the digits from its left and right inputs into a single number.
# Using your new knowledge of elephant hiding spots, determine which equations could possibly be true. What is their
# total calibration result?

import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data


def check_line(result, numbers, with_concatenations=False):
    nb = len(numbers)
    if nb == 1:
        return numbers[0] == result
    if with_concatenations:
        return any([
            check_line(result, [numbers[0] + numbers[1]] + numbers[2:], with_concatenations),
            check_line(result, [numbers[0] * numbers[1]] + numbers[2:], with_concatenations),
            check_line(result, [int(f'{numbers[0]}{numbers[1]}')] + numbers[2:], with_concatenations)
        ])
    return any([
        check_line(result, [numbers[0] + numbers[1]] + numbers[2:]),
        check_line(result, [numbers[0] * numbers[1]] + numbers[2:])
    ])


def calibration_result(calibration_equations, with_concatenation=False):
    return sum([
        equation[0] for equation in calibration_equations if check_line(equation[0], equation[1], with_concatenation)
    ])


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day07.txt', split=':')
    data = [[line[0], [int(x) for x in line[1].split(' ')[1:]]] for line in data]

    if star == 1:  # The final answer is: 932137732557
        solution = calibration_result(data)
    elif star == 2:  # The final answer is: 661823605105500
        solution = calibration_result(data, with_concatenation=True)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
