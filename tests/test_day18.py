import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day18


def test_sets():
    return [
        {
            'number': 1,
            'input': [
                [
                    [5, 4], [4, 2], [4, 5], [3, 0], [2, 1], [6, 3], [2, 4], [1, 5], [0, 6], [3, 3], [2, 6], [5, 1],
                    [1, 2], [5, 5], [2, 5], [6, 5], [1, 4], [0, 4], [6, 4], [1, 1], [6, 1], [1, 0], [0, 5], [1, 6],
                    [2, 0]
                ],
                6, 12
            ],
            'expected1': 22,
            'expected2': []
        },
    ]


def test_first_star(test_data, expected):
    solution = day18.exit_map(test_data[0], test_data[1], test_data[2])
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
