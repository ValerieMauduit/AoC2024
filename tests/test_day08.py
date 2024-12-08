import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day08


def test_sets():
    return [
        {
            'number': 1,
            'input': [
                '............', '........0...', '.....0......', '.......0....', '....0.......', '......A.....',
                '............', '............', '........A...', '.........A..', '............', '............'
            ],
            'expected1': 14,
            'expected2': []
        },
    ]


def test_first_star(test_data, expected):
    test_data = [[x for x in line] for line in test_data]
    solution = day08.count_all_antinodes(test_data)
    if solution != expected:
        print("Your output is:")
        print(solution)
        raise Exception(f'This is not the solution, you should get {expected}')
    print('--- Test OK')


def test_second_star(test_data, expected):
    solution = day00.my_func(test_data)
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
