#! /usr/bin/env python

import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day01


def test_sets():
    return [
        {
            'number': 1,
            'input': [[3, 4], [4, 3], [2, 5], [1, 3], [3, 9], [3, 3]],
            'expected1': 11,
            'expected2': 31,
        }
    ]


def test_first_star(positions, expected):
    solution = day01.distance_sum(positions)
    if solution != expected:
        print(f"Your output is: {solution}")
        raise Exception(f'This is not the solution, you should get {expected}')
    print('--- Test OK')


def test_second_star(positions, expected):
    solution = day01.comparisons(positions)
    if solution != expected:
        print(f"Your output is: {solution}")
        raise Exception(f'This is not the solution, you should get {expected}')
    print('--- Test OK')


def main():
    test_case = int(input('Which star to test? '))
    for test in test_sets():
        print(f"=== Test #{test['number']} ===")
        if test_case == 1:
            test_first_star(test['input'], test['expected1'])
        elif test_case == 2:
            test_second_star(test['input'], test['expected2'])
        else:
            print("Error, the star must be 1 or 2.")


if __name__ == '__main__':
    main()
