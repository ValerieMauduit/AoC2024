import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day19


def test_sets():
    return [
        {
            'number': 1,
            'input': {
                'towels': ['r', 'wr', 'b', 'g', 'bwu', 'rb', 'gb', 'br'],
                'patterns': ['brwrr', 'bggr', 'gbbr', 'rrbgbr', 'ubwu', 'bwurrg', 'brgr', 'bbrgwb']
            },
            'expected1': 6,
            'expected2': 16
        },
        {
            'number': 1,
            'input': {
                'towels': ['r', 'wr', 'b', 'g', 'bwu', 'rb', 'gb', 'br', 'bw', 'ur'],
                'patterns': ['brwrrbr', 'bggr', 'gbbr', 'rrbgbr', 'ubwu', 'bwurrg', 'brgr', 'bbrgwb']
            },
            'expected1': 6,
            'expected2': 21
        },
    ]


def test_first_star(test_data, expected):
    solution = day19.count_possible_patterns(test_data)
    if solution != expected:
        print("Your output is:")
        print(solution)
        raise Exception(f'This is not the solution, you should get {expected}')
    print('--- Test OK')


def test_second_star(test_data, expected):
    solution = day19.count_all_possibilities_for_all_patterns(test_data)
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
