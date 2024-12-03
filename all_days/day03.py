# Day03: Mull It Over

# First star:
# It seems like the goal of the program is just to multiply some numbers. It does that with instructions like mul(X,Y),
# where X and Y are each 1-3 digit numbers.
# However, because the program's memory has been corrupted, there are also many invalid characters that should be
# ignored, even if they look like part of a mul instruction.
# Adding up the result of each instruction produces the result.

# Second star: There are two new instructions you'll need to handle:
# - The do() instruction enables future mul instructions.
# - The don't() instruction disables future mul instructions.
# Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are
# enabled.

import os
import sys
import re
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data


def scan(text):
    return re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", text)


def get_result(texts):
    split = [formula.split(',') for formula in texts]
    return sum([int(pair[0][4:]) * int(pair[1][:-1]) for pair in split])


def applying_instructions(text):
    do_s = text.split('do()')
    instructions = [instruction.split("don't()")[0] for instruction in do_s]
    return ' '.join(instructions)


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day03.txt', numbers=False)

    if star == 1:  # The final answer is: 179571322
        solution = get_result(scan(' '.join(data)))
    elif star == 2:  # The final answer is: 103811193
        solution = get_result(scan(applying_instructions(' '.join(data))))
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
