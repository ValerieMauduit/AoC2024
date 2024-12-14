import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day10
from AoC_tools.work_with_maps import AocMap


def test_sets():
    return [
        {
            'number': 1,
            'input': [
                [8, 9, 0, 1, 0, 1, 2, 3], [7, 8, 1, 2, 1, 8, 7, 4], [8, 7, 4, 3, 0, 9, 6, 5], [9, 6, 5, 4, 9, 8, 7, 4],
                [4, 5, 6, 7, 8, 9, 0, 3], [3, 2, 0, 1, 9, 0, 1, 2], [0, 1, 3, 2, 9, 8, 0, 1], [1, 0, 4, 5, 6, 7, 3, 2]
            ],
            'expected1': 36,
            'expected2': []
        },
    ]


def test_first_star(test_data, expected):
    solution = day10.count_paths(AocMap(test_data, numbers=True))
    if solution != expected:
        print("Your output is:")
        print(solution)
        raise Exception(f'This is not the solution, you should get {expected}')
    print('--- Test OK')


def test_second_star(test_data, expected):
    solution = day10.my_func(test_data)
    if solution != expected:
        print("Your output is:")
        print(solution)
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
